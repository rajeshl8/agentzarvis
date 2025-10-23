# Placeholder for NVIDIA Retrieval Embedding NIM client.
# Implement: index_documents(s3_uri or local), search(query), and get_context(keys).
class RetrievalClient:
    def __init__(self, endpoint: str | None = None):
        self.endpoint = endpoint
    def index(self, docs: list[dict]): ...
    def search(self, query: str) -> list[dict]: return []
