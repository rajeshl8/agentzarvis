def summarize_meeting(text: str) -> dict:
    """Extract simple summary/actions from text (stub)."""
    summary = text[:180] + ("..." if len(text) > 180 else "")
    decisions = ["Share KPI deck today"] if "KPI" in text or "deck" in text else []
    actions = [{"owner":"Rajesh","task":"Follow up email","due":"today"}]
    return {"summary": summary, "decisions": decisions, "actions": actions}
