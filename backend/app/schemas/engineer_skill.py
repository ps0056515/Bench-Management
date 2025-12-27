from pydantic import BaseModel

class EngineerSkillCreate(BaseModel):
    engineer_id: int
    skill_id: int
    current_level: int
    confidence: float

class EngineerSkillResponse(EngineerSkillCreate):
    id: int
    class Config:
        from_attributes = True
