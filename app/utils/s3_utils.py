import os, json
from pathlib import Path
from typing import Tuple

LOCAL_DATA_DIR = Path(os.getenv("LOCAL_DATA_DIR", "data_samples"))

def load_demo_data() -> Tuple[list, str, str, dict]:
    emails = json.loads((LOCAL_DATA_DIR / "emails.json").read_text(encoding="utf-8"))
    calendar_ics = (LOCAL_DATA_DIR / "calendar.ics").read_text(encoding="utf-8")
    meeting_txt = (LOCAL_DATA_DIR / "meeting.txt").read_text(encoding="utf-8")
    profile = json.loads((LOCAL_DATA_DIR / "profile.json").read_text(encoding="utf-8"))
    return emails, calendar_ics, meeting_txt, profile

def load_from_s3(bucket: str, prefix: str = "demo/"):
    import boto3
    s3 = boto3.client("s3", region_name=os.getenv("AWS_REGION","us-east-1"))
    def _get(key):
        obj = s3.get_object(Bucket=bucket, Key=key)
        return obj["Body"].read().decode("utf-8")
    emails = json.loads(_get(prefix + "emails.json"))
    calendar_ics = _get(prefix + "calendar.ics")
    meeting_txt = _get(prefix + "meeting.txt")
    profile = json.loads(_get(prefix + "profile.json"))
    return emails, calendar_ics, meeting_txt, profile
