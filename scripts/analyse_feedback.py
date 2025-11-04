# backend/scripts/analyze_feedback.py
import os
import json
from collections import Counter

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FEEDBACK_PATH = os.path.join(BASE, "data", "feedback", "feedback_log.jsonl")

def read_feedback(path):
    if not os.path.exists(path):
        print("No feedback file found at:", path)
        return []
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line=line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except Exception:
                continue
    return rows

def analyze(rows):
    n = len(rows)
    if n == 0:
        print("No feedback rows to analyze.")
        return
    # Expect feedback entries to contain keys:
    # 'system_flagged_as_phish' and 'user_says_phish'
    agree = 0
    sys_flag_count = 0
    user_flag_count = 0
    for r in rows:
        sf = r.get("system_flagged_as_phish")
        us = r.get("user_says_phish")
        if sf: sys_flag_count += 1
        if us: user_flag_count += 1
        if sf == us:
            agree += 1

    print("Feedback rows:", n)
    print("System flagged as phish:", sys_flag_count)
    print("Users marked phish:", user_flag_count)
    print("Agreement (system == user):", agree, f"({agree/n:.2%})")

    # If entries contain 'notes', show top few
    notes = [r.get("notes", "") for r in rows if r.get("notes")]
    if notes:
        print("\nSample notes:")
        for s in notes[:5]:
            print("-", s)

    # Added summary with accuracy
    total_feedback = n
    system_correct = agree
    accuracy = system_correct / total_feedback * 100
    print("\n--- Summary ---")
    print(f"Total feedback entries: {total_feedback}")
    print(f"System matches user feedback: {system_correct} ({accuracy:.2f}%)")

if __name__ == "__main__":
    rows = read_feedback(FEEDBACK_PATH)
    analyze(rows)
