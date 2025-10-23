# API Contract (v1)

**Endpoint:** `POST /brief`

## Request JSON
```json
{
  "emails": [{"from": "", "subject": "", "body": ""}],
  "calendar_ics": "BEGIN:VCALENDAR...END:VCALENDAR",
  "meeting_text": "free-form transcript or notes"
}
```

## Response JSON
```json
{
  "priorities": [{"title":"", "why":""}],
  "draft_replies": [{"subject":"", "reply":""}],
  "plan": [{"time":"HH:MM", "item":""}],
  "meeting": {
    "summary":"",
    "decisions":[],
    "actions":[{"owner":"", "task":"", "due":""}]
  }
}
```

This contract must remain stable during the hackathon so Frontend and Backend can work independently.
