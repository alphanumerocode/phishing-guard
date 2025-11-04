import json

FEEDBACK_PATH = "data/feedback/feedback_log.jsonl"

with open(FEEDBACK_PATH, "r", encoding="utf-8") as f:
    for line in f:
        entry = json.loads(line.strip())
        print(json.dumps(entry, indent=2))
