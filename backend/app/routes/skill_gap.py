from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.services.skill_gap_service import calculate_skill_gap

router = APIRouter(prefix="/gap", tags=["Skill Gap"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{engineer_id}/{demand_id}")
def skill_gap(engineer_id: int, demand_id: int, db: Session = Depends(get_db)):
    return calculate_skill_gap(db, engineer_id, demand_id)
