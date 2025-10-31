from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.brief import router as brief_router

app = FastAPI(title="AgentZarvis API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(brief_router)
