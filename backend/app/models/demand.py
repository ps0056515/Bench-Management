from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Demand(Base):
    __tablename__ = "demands"

    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String, nullable=False)
    required_skills = Column(String, nullable=False)
    min_experience = Column(Integer, nullable=False)
    location = Column(String, nullable=False)
    status = Column(String, nullable=False)
