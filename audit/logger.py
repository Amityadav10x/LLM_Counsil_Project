import json
from datetime import datetime

def log(event: dict):
    """
    Append an audit event to an append-only JSONL log file.
    """
    with open("audit_log.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps({
            "timestamp": datetime.utcnow().isoformat(),
            "event": event
        }) + "\n")
