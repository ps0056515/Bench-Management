from sqlalchemy.orm import Session
from app.models.bench_employee import BenchEmployee
from app.schemas.bench_employee import BenchEmployeeCreate

def create_employee(db: Session, emp: BenchEmployeeCreate):
    employee = BenchEmployee(**emp.model_dump())
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee

def get_all_employees(db: Session):
    return db.query(BenchEmployee).all()


def update_employee_by_id(db: Session, emp_id: int, emp):
    employee = db.query(BenchEmployee).filter(BenchEmployee.id == emp_id).first()
    if not employee:
        return None

    employee.name = emp.name
    employee.primary_skills = emp.primary_skills
    employee.secondary_skills = emp.secondary_skills
    employee.experience_years = emp.experience_years
    employee.location = emp.location
    employee.status = emp.status

    db.commit()
    db.refresh(employee)
    return employee


def delete_employee_by_id(db: Session, emp_id: int):
    employee = db.query(BenchEmployee).filter(BenchEmployee.id == emp_id).first()
    if employee:
        db.delete(employee)
        db.commit()
