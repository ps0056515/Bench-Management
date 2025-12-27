from sqlalchemy import Column, Integer, ForeignKey, String
from app.db.base import Base

class DemandSkill(Base):
    __tablename__ = "demand_skills"

    id = Column(Integer, primary_key=True, index=True)
    demand_id = Column(Integer, ForeignKey("demands.id"))
    skill_id = Column(Integer, ForeignKey("skills.id"))
    required_level = Column(Integer)  # 1–4
    priority = Column(String)         # LOW | MEDIUM | HIGH
