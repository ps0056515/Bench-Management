from pydantic import BaseModel

class DemandCreate(BaseModel):
    project_name: str
    required_skills: str
    min_experience: int
    location: str
    status: str

class DemandResponse(DemandCreate):
    id: int

    class Config:
        from_attributes = True
