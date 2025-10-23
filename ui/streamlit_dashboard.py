import streamlit as st, json, requests

st.set_page_config(page_title="AgentZarvis — Daily Executive Brief", layout="wide")
st.title("AgentZarvis — Daily Executive Brief")

# Inputs (editable)
emails_str = st.text_area("emails.json", value=json.dumps([
  {"from":"ceo@startup.io","subject":"Board prep","body":"KPIs + runway by tonight"},
  {"from":"ops@vendor.com","subject":"Invoice overdue","body":"INV-2048 due 10/25"}
], indent=2), height=160)

calendar_ics = st.text_area("calendar.ics", value="""BEGIN:VCALENDAR
BEGIN:VEVENT
DTSTART:20251022T090000
DTEND:20251022T093000
SUMMARY:Standup
END:VEVENT
BEGIN:VEVENT
DTSTART:20251022T110000
DTEND:20251022T120000
SUMMARY:Investor call (VC Partner)
LOCATION:Zoom
END:VEVENT
BEGIN:VEVENT
DTSTART:20251022T150000
DTEND:20251022T160000
SUMMARY:Customer security review
END:VEVENT
END:VCALENDAR
""", height=180)

meeting_text = st.text_area("meeting.txt", value="Investor call: Need MRR, churn, CAC, runway. Action: send KPI deck today; schedule Friday follow-up.", height=100)

colA, colB = st.columns([1,1])
with colA:
    st.caption("Toggle between mock mode and API mode")
    use_api = st.toggle("Use API mode", value=False)

if st.button("Generate Brief"):
    if use_api:
        payload = {"emails": json.loads(emails_str), "calendar_ics": calendar_ics, "meeting_text": meeting_text}
        data = requests.post("http://localhost:8000/brief", json=payload, timeout=30).json()
    else:
        import pathlib, json as _json
        mock_path = pathlib.Path(__file__).with_name("mock_response.json")
        data = _json.loads(mock_path.read_text())

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Priorities")
        for p in data.get("priorities", []):
            st.write(f"- **{p.get('title','')}** — {p.get('why','')}")
        st.subheader("Draft Replies")
        for d in data.get("draft_replies", []):
            st.code(d.get("reply",""))

    with col2:
        st.subheader("Today’s Plan")
        st.table(data.get("plan", []))
        st.subheader("Meeting Summary")
        mtg = data.get("meeting", {})
        st.write(mtg.get("summary",""))
        st.write("**Decisions:**")
        st.write("\n".join([f"- {x}" for x in mtg.get("decisions", [])]) or "-")
        st.write("**Actions:**")
        st.table(mtg.get("actions", []))
