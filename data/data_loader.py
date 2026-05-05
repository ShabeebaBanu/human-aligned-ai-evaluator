import pandas as pd
import os, requests
from config import (
  SHEET_URL, 
  TIMESTAMP,
  BASE_PATH,
  RAW_DATA_PATH,
  FEATURE_DATA_PATH,
  PREPROCESSED_DATA_PATH,
  RAW_FILE,
  PROCESSED_FILE,
  FEATURES_FILE,
  FEATURE_CONCEPT_COVERAGE_PATH,
  FEATURE_CONTRADICTION_PATH,
  FEATURE_REASONING_PATH,
  FEATURE_SEMENTIC_SIMILARITY_PATH,
  FEATURE_CONCEPT_COVERAGE_FILE,
  FEATURE_CONTRADICTION_FILE,
  FEATURE_REASONING_FILE,
  FEATURE_SEMENTIC_SIMILARITY_FILE
)
from datetime import datetime

def _get_path(folderPath, filename):
  return os.path.join(BASE_PATH, folderPath, filename);

def _needs_sync():
  if not os.path.exists(TIMESTAMP): return True
  with open(TIMESTAMP) as f:
    age = datetime.now().timestamp() - float(f.read())
  return age > 3600

# ......................................................................................................
# RAW DATA
# ......................................................................................................

def _sync_raw_data():
  """Fetch dataset from Google Sheets and save to raw folder"""
  os.makedirs(os.path.join(BASE_PATH, RAW_DATA_PATH), exist_ok=True)

  print("Syncing raw dataset from Google Sheets...")

  response = requests.get(SHEET_URL, timeout=10)
  response.raise_for_status()

  raw_path = _get_path(RAW_DATA_PATH, RAW_FILE)

  with open(raw_path, "wb") as f:
      f.write(response.content)

  with open(TIMESTAMP, "w") as f:
      f.write(str(datetime.now().timestamp()))

  print("Sync completed.")
  
  
def load_raw_data(force_sync=False):
    """
    Load original dataset (from Google Sheets)
    """
    raw_path = _get_path(RAW_DATA_PATH, RAW_FILE)

    try:
        if force_sync or _needs_sync():
            _sync_raw_data()
        else:
            print("Using local raw dataset.")
    except Exception as e:
        print(f"Sync failed: {e}")
        print("Using existing local raw dataset.")

    if not os.path.exists(raw_path):
        raise FileNotFoundError(f"Raw dataset not found: {raw_path}")

    return pd.read_csv(raw_path)
  

# ......................................................................................................
# PREPROCESSED DATA
# ......................................................................................................

  
def load_preprocessed_data():
    path = _get_path(PREPROCESSED_DATA_PATH, PROCESSED_FILE)

    if not os.path.exists(path):
        raise FileNotFoundError(f"Processed data not found: {path}")

    return pd.read_csv(path)
  
def save_processed_data(df):
    os.makedirs(os.path.join(BASE_PATH, PREPROCESSED_DATA_PATH), exist_ok=True)
    path = _get_path(PREPROCESSED_DATA_PATH, PROCESSED_FILE)
    
    # CSV path
    csv_path = _get_path(PREPROCESSED_DATA_PATH, PROCESSED_FILE)

    # Excel path (replace .csv → .xlsx)
    excel_path = csv_path.replace(".csv", ".xlsx")

    # Save CSV (main)
    df.to_csv(csv_path, index=False)

    # Save Excel (extra)
    df.to_excel(excel_path, index=False)
    
    print(f"Processed data saved → {path}")
    
# ......................................................................................................
# FEATURES DATA
# ......................................................................................................

def load_feature(split=None):
    path = _get_path(FEATURE_DATA_PATH, FEATURES_FILE)

    if not os.path.exists(path):
        raise FileNotFoundError(f"Features data not found: {path}")

    df = pd.read_csv(path)

    # if split:
    #     if "split" not in df.columns:
    #         raise ValueError("Features dataset must contain 'split' column")

    #     df = df[df["split"] == split].reset_index(drop=True)

    return df
  
def save_feature(df):
    os.makedirs(os.path.join(BASE_PATH, FEATURE_DATA_PATH), exist_ok=True)
    path = _get_path(FEATURE_DATA_PATH, FEATURES_FILE)
    df.to_csv(path, index=False)
    print(f"Features saved → {path}")
    

# ......................................................................................................
# FEATURES DATA - CONCEPT COVERAGE
# ......................................................................................................

def save_feature_concept_coverage(df):
    os.makedirs(os.path.join(BASE_PATH, FEATURE_DATA_PATH, FEATURE_CONCEPT_COVERAGE_PATH), exist_ok=True)
    path = _get_path(FEATURE_CONCEPT_COVERAGE_PATH, FEATURE_CONCEPT_COVERAGE_FILE)
    df.to_csv(path, index=False)
    print(f"Feature concept coverage saved → {path}") 
    

# ......................................................................................................
# FEATURES DATA - SEMENTIC SIMILARITY
# ......................................................................................................
  
def save_feature_sementic_similarity(df):
    os.makedirs(os.path.join(BASE_PATH, FEATURE_DATA_PATH, FEATURE_SEMENTIC_SIMILARITY_PATH), exist_ok=True)
    path = _get_path(FEATURE_SEMENTIC_SIMILARITY_PATH, FEATURE_SEMENTIC_SIMILARITY_FILE)
    df.to_csv(path, index=False)
    print(f"Feature sementic similarity saved → {path}")
    

# ......................................................................................................
# FEATURES DATA - REASONING QUALITY
# ......................................................................................................   

def save_feature_reasoning_quality(df):
    os.makedirs(os.path.join(BASE_PATH, FEATURE_DATA_PATH, FEATURE_REASONING_PATH), exist_ok=True)
    path = _get_path(FEATURE_REASONING_PATH, FEATURE_REASONING_FILE)
    df.to_csv(path, index=False)
    print(f"Feature reasoning quality saved → {path}")
    

# ......................................................................................................
# FEATURES DATA - CONTRADICTION
# ......................................................................................................   

def save_feature_contradiction(df):
    os.makedirs(os.path.join(BASE_PATH, FEATURE_DATA_PATH, FEATURE_CONTRADICTION_PATH), exist_ok=True)
    path = _get_path(FEATURE_CONTRADICTION_PATH, FEATURE_CONTRADICTION_FILE)
    df.to_csv(path, index=False)
    print(f"Feature contradiction saved → {path}")