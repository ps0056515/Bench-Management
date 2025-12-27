from sqlalchemy.orm import Session
from app.models.bench_employee import BenchEmployee
from app.schemas.bench_employee import BenchEmployeeCreate

def create_employee(db: Session, emp: BenchEmployeeCreate):
    employee = BenchEmployee(**emp.dict())
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee

def get_all_employees(db: Session):
    return db.query(BenchEmployee).all()
