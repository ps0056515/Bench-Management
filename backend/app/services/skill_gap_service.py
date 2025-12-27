from sqlalchemy.orm import Session
from app.models.engineer_skill import EngineerSkill
from app.models.demand_skill import DemandSkill

def calculate_skill_gap(db: Session, engineer_id: int, demand_id: int):
    engineer_skills = db.query(EngineerSkill).filter_by(engineer_id=engineer_id).all()
    demand_skills = db.query(DemandSkill).filter_by(demand_id=demand_id).all()

    result = []

    for d in demand_skills:
        e = next((x for x in engineer_skills if x.skill_id == d.skill_id), None)

        current = e.current_level if e else 0
        gap = d.required_level - current

        result.append({
            "skill_id": d.skill_id,
            "current_level": current,
            "required_level": d.required_level,
            "gap": gap,
            "status": "READY" if gap <= 0 else "UPS KILL"
        })

    return result
