from pydantic import BaseModel, Field

class EmployeePredictionRequest(BaseModel):
    """Pydantic model to validate incoming employee data before ML prediction."""
    employee_id: int
    age: int = Field(..., ge=18, le=100, description="Age must be between 18 and 100")
    department: str
    job_satisfaction: int = Field(..., ge=1, le=5)
    engagement_score: int = Field(..., ge=0, le=100)