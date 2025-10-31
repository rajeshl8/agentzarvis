from typing import List, Dict
import time

class ActionAgent:
    def execute_plan(self, approved_tasks: List[Dict]) -> Dict:
        logs = []
        for item in approved_tasks:
            logs.append(f"✅ Executed: {item['task']}")
            time.sleep(0.02)
        return {"executed": logs}
