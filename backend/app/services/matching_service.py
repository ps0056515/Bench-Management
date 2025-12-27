from sqlalchemy.orm import Session
from app.models.bench_employee import BenchEmployee
from app.models.demand import Demand
from app.core.config import settings
from anthropic import Anthropic
import json

client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)

def match_demand_to_bench(db: Session, demand_id: int):
    demand = db.query(Demand).filter(Demand.id == demand_id).first()
    if not demand:
        return []

    employees = db.query(BenchEmployee).all()
    results = []

    for emp in employees:
        prompt = f"""
You are a staffing matching engine.

Bench Employee:
Skills: {emp.primary_skills}
Experience: {emp.experience_years} years
Location: {emp.location}

Demand Requirements:
Skills: {demand.required_skills}
Minimum Experience: {demand.min_experience} years
Location: {demand.location}

Return STRICT JSON ONLY:
{{
  "match_score": number,
  "skill_match": "LOW | MEDIUM | HIGH",
  "experience_fit": "LOW | MEDIUM | HIGH",
  "final_decision": "RECOMMEND | HOLD | REJECT",
  "reason": "one sentence"
}}
"""

        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=300,
            messages=[{"role": "user", "content": prompt}]
        )

        raw = response.content[0].text.strip()

        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            continue  # fail-safe: skip bad LLM response

        if parsed.get("match_score", 0) >= 70:
            results.append({
                "employee_id": emp.id,
                "employee_name": emp.name,
                "score": parsed["match_score"],
                "decision": parsed["final_decision"],
                "reason": parsed["reason"]
            })

    return sorted(results, key=lambda x: x["score"], reverse=True)
