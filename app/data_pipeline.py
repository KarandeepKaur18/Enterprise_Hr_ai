import pandas as pd
from pathlib import Path

def load_raw_data(file_name: str) -> pd.DataFrame:
    """Loads raw CSV data dynamically regardless of OS."""
    # Tech magic: Pathlib avoids messy string concatenations for paths
    base_dir = Path(__file__).resolve().parent.parent
    file_path = base_dir / "data" / "raw" / file_name
    
    print(f"Loading data from: {file_path}")
    return pd.read_csv(file_path)

def preprocess_attrition_data(df: pd.DataFrame) -> pd.DataFrame:
    """Handles missing values and basic encoding."""
    # If the dataframe is empty (just headers right now), safely return
    if df.empty:
        print("Warning: DataFrame is empty. Add some dummy rows later!")
        return df
        
    # Quick pandas hack to fill NaNs across the whole dataframe
    clean_df = df.fillna("Unknown")
    return clean_df

def run_ingestion():
    """Main function to trigger the pipeline."""
    df = load_raw_data("employee_attrition.csv")
    processed_df = preprocess_attrition_data(df)
    print(f"Pipeline executed! Final Data Shape: {processed_df.shape}")

if __name__ == "__main__":
    run_ingestion()