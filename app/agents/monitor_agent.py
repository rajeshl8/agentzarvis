from typing import List, Dict

class MonitorAgent:
    def verify_progress(self, plan: List[Dict]) -> str:
        pending = [t for t in plan if t.get('status') != 'done']
        if not pending:
            return "All tasks completed!"
        return f"{len(pending)} tasks still pending."
