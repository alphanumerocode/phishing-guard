# backend/scripts/seed_data.py
import os
import csv

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_PROCESSED = os.path.join(BASE, "data", "processed")
os.makedirs(DATA_PROCESSED, exist_ok=True)

OUT_CSV = os.path.join(DATA_PROCESSED, "emails_labeled.csv")

sample_rows = [
    ("Urgent: Verify your account", "Your account has been locked. Click https://example.com/verify to unlock.", 1),
    ("Meeting notes", "Attached are the notes from today's meeting. Please review.", 0),
    ("You won a prize!", "Congratulations! Claim now: http://claim-prize.example.com", 1),
    ("Project update", "The project deliverables are updated in the drive.", 0),
    ("Bank alert", "We noticed suspicious activity. Login at http://bank.example.verify.com", 1),
    ("Team lunch", "Who's up for lunch at 1pm today?", 0),
]

def write_csv(path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["subject", "body", "label"])
        for s,b,l in sample_rows:
            writer.writerow([s, b, l])
    print(f"Created sample CSV at: {path}")

if __name__ == "__main__":
    write_csv(OUT_CSV)
