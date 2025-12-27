from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.services.matching_service import match_demand_to_bench

router = APIRouter(
    prefix="/match",
    tags=["Match"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{demand_id}")
def match(demand_id: int, db: Session = Depends(get_db)):
    return match_demand_to_bench(db, demand_id)
