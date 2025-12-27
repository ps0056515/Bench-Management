from sqlalchemy import Column, Integer, ForeignKey, Float
from app.db.base import Base

class EngineerSkill(Base):
    __tablename__ = "engineer_skills"

    id = Column(Integer, primary_key=True, index=True)
    engineer_id = Column(Integer, ForeignKey("bench_employees.id"))
    skill_id = Column(Integer, ForeignKey("skills.id"))
    current_level = Column(Integer)  # 1–4
    confidence = Column(Float)        # 0–1
