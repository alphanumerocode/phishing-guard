# Example: read raw CSV and clean text
import pandas as pd
import os

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RAW_CSV = os.path.join(BASE, "raw", "emails_raw.csv")
PROCESSED_CSV = os.path.join(BASE, "processed", "emails_labeled.csv")

if os.path.exists(RAW_CSV):
    df = pd.read_csv(RAW_CSV)
    df['subject'] = df['subject'].fillna('')
    df['body'] = df['body'].fillna('')
    # Simple cleaning: remove extra spaces
    df['subject'] = df['subject'].str.strip()
    df['body'] = df['body'].str.strip()
    df.to_csv(PROCESSED_CSV, index=False)
    print(f"Processed emails saved at: {PROCESSED_CSV}")
else:
    print(f"No raw CSV found at {RAW_CSV}. You can manually create one or use seed_data.py.")
