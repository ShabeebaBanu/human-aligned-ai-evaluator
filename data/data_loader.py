import pandas as pd
import os, requests
from config import SHEET_URL, LOCAL_PATH, TIMESTAMP
from datetime import datetime

def _needs_sync():
  if not os.path.exists(TIMESTAMP): return True
  with open(TIMESTAMP) as f:
    age = datetime.now().timestamp() - float(f.read())
  return age > 3600

def _sync():
  os.makedirs("data", exist_ok=True)
  print("Syncing from Google Sheets...")
  r = requests.get(SHEET_URL, timeout=10)
  r.raise_for_status()
  with open(LOCAL_PATH, "wb") as f: f.write(r.content)
  with open(TIMESTAMP, "w") as f: f.write(str(datetime.now().timestamp()))
  print(f"Sync done at {datetime.now().strftime('%H:%M:%S')}")

def load_dataset(split=None, force_sync=False):
  """
  split = None → returns the full dataset (all rows)
  split = 'train' → only training rows
  split = 'test' → only test rows
  split = 'validation' → only validation rows
  force_sync = True → re-download from sheet right now
  """
  
  try:
    if force_sync or _needs_sync(): _sync()
    else: print("Dataset up to date — using local copy.")
  except Exception as e:
    print(f"Sync failed ({e}). Using local copy.")
    
  df = pd.read_csv(LOCAL_PATH)
  
  if split is not None:
    if split not in ['train','test','validation']:
      raise ValueError(f"split must be 'train', 'test', or 'validation'. Got: {split}")
    df = df[df['split'] == split].reset_index(drop=True)
  return df