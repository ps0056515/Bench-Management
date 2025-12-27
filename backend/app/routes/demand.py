from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.session import SessionLocal
from app.services.demand_service import create_demand, get_all_demands, update_demand_by_id, delete_demand_by_id
from app.schemas.demand import DemandCreate, DemandResponse

router = APIRouter(prefix="/demand", tags=["Demand"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=DemandResponse)
def add_demand(demand: DemandCreate, db: Session = Depends(get_db)):
    return create_demand(db, demand)

@router.get("/", response_model=List[DemandResponse])
def list_demands(db: Session = Depends(get_db)):
    return get_all_demands(db)

@router.put("/{demand_id}", response_model=DemandResponse)
def update_demand(
    demand_id: int,
    demand: DemandCreate,
    db: Session = Depends(get_db)
):
    return update_demand_by_id(db, demand_id, demand)


@router.delete("/{demand_id}")
def delete_demand(demand_id: int, db: Session = Depends(get_db)):
    delete_demand_by_id(db, demand_id)
    return {"message": "Demand deleted"}
