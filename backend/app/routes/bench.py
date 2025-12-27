from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.session import SessionLocal
from app.services.bench_service import create_employee, get_all_employees, update_employee_by_id, delete_employee_by_id
from app.schemas.bench_employee import BenchEmployeeCreate, BenchEmployeeResponse

router = APIRouter(prefix="/bench", tags=["Bench"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=BenchEmployeeResponse)
def add_employee(emp: BenchEmployeeCreate, db: Session = Depends(get_db)):
    return create_employee(db, emp)

@router.get("/", response_model=List[BenchEmployeeResponse])
def list_employees(db: Session = Depends(get_db)):
    return get_all_employees(db)

@router.put("/{emp_id}", response_model=BenchEmployeeResponse)
def update_employee(
    emp_id: int,
    emp: BenchEmployeeCreate,
    db: Session = Depends(get_db)
):
    return update_employee_by_id(db, emp_id, emp)


@router.delete("/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    delete_employee_by_id(db, emp_id)
    return {"message": "Bench employee deleted"}
