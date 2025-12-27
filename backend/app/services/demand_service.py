from sqlalchemy.orm import Session
from app.models.demand import Demand
from app.schemas.demand import DemandCreate

def create_demand(db: Session, demand: DemandCreate):
    d = Demand(**demand.model_dump())
    db.add(d)
    db.commit()
    db.refresh(d)
    return d

def get_all_demands(db: Session):
    return db.query(Demand).all()

def update_demand_by_id(db: Session, demand_id: int, demand):
    d = db.query(Demand).filter(Demand.id == demand_id).first()
    if not d:
        return None

    d.project_name = demand.project_name
    d.required_skills = demand.required_skills
    d.min_experience = demand.min_experience
    d.location = demand.location
    d.status = demand.status

    db.commit()
    db.refresh(d)
    return d


def delete_demand_by_id(db: Session, demand_id: int):
    d = db.query(Demand).filter(Demand.id == demand_id).first()
    if d:
        db.delete(d)
        db.commit()
