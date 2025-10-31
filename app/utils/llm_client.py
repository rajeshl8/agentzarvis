import os

class LLMClient:
    def __init__(self):
        self.base = os.getenv("NIM_BASE_URL_LLM","http://nim-llm-placeholder")
        self.key = os.getenv("NIM_API_KEY","demo-key")

    async def chat(self, messages, model="nvidia/llama-3.1-nemotron-nano-8b-instruct"):
        return "Mocked response from LLM (replace with NIM call)."
