from fastapi import FastAPI
from app.validation.employee_schema import EmployeePredictionRequest
import logging

# Step 20: Simple Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")

app = FastAPI(title="Agentic HRMS Platform", version="1.0")

@app.get("/")
def root_check():
    return {"status": "online", "message": "Welcome to the Enterprise HR AI!"}

@app.get("/dashboard/summary")
def dashboard_summary():
    return {
        "total_employees": 2500,
        "high_risk_employees": 124,
        "average_engagement": 72
    }

@app.post("/predict/attrition")
def predict_attrition(employee: EmployeePredictionRequest):
    """
    Accepts employee data, validates it, and will eventually return a risk score.
    """
    logging.info(f"Prediction request received for Employee ID: {employee.employee_id}")
    
    # We will hook up the actual ML model here later. 
    # For now, returning a mock response to test the endpoint!
    return {
        "employee_id": employee.employee_id,
        "predicted_attrition_risk": 0.82,
        "risk_level": "HIGH",
        "status": "success"
    }