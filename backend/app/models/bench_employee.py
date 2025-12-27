from sqlalchemy import Column, Integer, String, Date
from app.db.base import Base

class BenchEmployee(Base):
    __tablename__ = "bench_employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    primary_skills = Column(String, nullable=False)
    secondary_skills = Column(String, nullable=True)
    experience_years = Column(Integer, nullable=False)
    bench_start_date = Column(Date, nullable=False)
    location = Column(String, nullable=False)
    status = Column(String, nullable=False)
