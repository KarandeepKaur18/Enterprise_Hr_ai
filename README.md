# 🚀 Agentic HRMS: Enterprise Workforce Intelligence

An end-to-end AI-powered Human Resource Management System (HRMS) designed to predict employee attrition, identify critical skill gaps, and provide actionable upskilling recommendations. 

This platform moves beyond simple dashboards by utilizing machine learning and workforce intelligence to actively recommend interventions, bridging the gap between raw data and strategic HR decisions.

---

## 🛠️ Tech Stack & Architecture

This project was built with a structured, practical approach focusing on modularity and rapid deployment:

*   **Data Engineering:** Pandas, Python
*   **Machine Learning:** Scikit-learn (Random Forest, Logistic Regression), XGBoost
*   **Model Explainability:** SHAP (SHapley Additive exPlanations)
*   **Backend API:** FastAPI, Pydantic (Data Validation), Uvicorn
*   **Frontend UI:** Streamlit

---

## 🧠 Core Features

1.  **Attrition Prediction Engine:** Uses a trained Random Forest classifier to predict the probability of an employee leaving the company based on satisfaction, engagement, and experience metrics.
2.  **Explainable AI (XAI):** Integrates SHAP to provide HR managers with the specific reasons *why* a particular employee is flagged as high-risk.
3.  **Skill Gap Analyzer:** Automatically compares an employee's current tech stack against their target role requirements using high-speed set logic.
4.  **Actionable Upskilling:** Maps organizational skill gaps to specific learning modules and training courses.
5.  **Live Enterprise Dashboard:** A real-time Streamlit interface powered by a robust FastAPI backend.

---

## 💻 How to Run Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/Agentic-HRMS.git](https://github.com/YOUR_USERNAME/Agentic-HRMS.git)
cd Agentic-HRMS
