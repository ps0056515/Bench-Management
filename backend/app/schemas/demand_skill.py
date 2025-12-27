from pydantic import BaseModel

class DemandSkillCreate(BaseModel):
    demand_id: int
    skill_id: int
    required_level: int
    priority: str

class DemandSkillResponse(DemandSkillCreate):
    id: int
    class Config:
        from_attributes = True
