from pydantic import BaseModel
from datetime import date
from typing import Optional

class BenchEmployeeBase(BaseModel):
    name: str
    primary_skills: str
    secondary_skills: Optional[str] = None
    experience_years: int
    bench_start_date: date
    location: str
    status: str

class BenchEmployeeCreate(BenchEmployeeBase):
    pass

class BenchEmployeeUpdate(BaseModel):
    primary_skills: Optional[str] = None
    secondary_skills: Optional[str] = None
    experience_years: Optional[int] = None
    location: Optional[str] = None
    status: Optional[str] = None

class BenchEmployeeResponse(BenchEmployeeBase):
    id: int

    class Config:
        from_attributes = True
