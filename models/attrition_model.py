import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import sys
from pathlib import Path

# Temporarily append app folder to path so we can import our pipeline
sys.path.append(str(Path(__file__).resolve().parent.parent))
from app.data_pipeline import load_raw_data, preprocess_attrition_data

def train_attrition_model(df: pd.DataFrame):
    """Trains the attrition prediction model to output a risk scale."""
    print("Initializing tech magic... converting text to numbers!")
    
    # One-hot encoding right inside the function
    df_encoded = pd.get_dummies(df, columns=["Department", "Role", "InternalMobility"])
    
    # Splitting features (X) and target (y)
    X = df_encoded.drop(columns=["EmployeeID", "RiskLabel"])
    y = df_encoded["RiskLabel"]
    
    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the Random Forest
    print("Training Random Forest Classifier...")
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    
    print(f"Model successfully trained! Accuracy: {acc * 100}%")
    return model

if __name__ == "__main__":
    # Pull data using our existing pipeline
    raw_df = load_raw_data("employee_attrition.csv")
    clean_df = preprocess_attrition_data(raw_df)
    
    # Train the model
    trained_model = train_attrition_model(clean_df)