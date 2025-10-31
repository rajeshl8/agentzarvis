import os
from typing import List

class RetrievalClient:
    def __init__(self):
        self.base = os.getenv("NIM_BASE_URL_EMB","http://nim-emb-placeholder")
        self.key = os.getenv("NIM_API_KEY","demo-key")

    async def embed_texts(self, texts: List[str]):
        return [[0.1,0.2,0.3,0.4] for _ in texts]
