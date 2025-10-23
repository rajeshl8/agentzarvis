def summarize_and_draft(emails: list[dict]) -> dict:
    """Return {'priorities': [...], 'draft_replies': [...]} — stub for hackathon MVP."""
    priorities = []
    drafts = []
    for e in emails[:5]:
        prio = {"title": e.get("subject","").strip() or "Email", "why": f"From {e.get('from','unknown')}"}
        priorities.append(prio)
        drafts.append({"subject": e.get("subject",""), "reply": f"Hi, regarding '{e.get('subject','')}', thanks—will revert shortly. —Rajesh"})
    return {"priorities": priorities, "draft_replies": drafts}
