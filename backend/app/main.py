from fastapi import FastAPI
from api.health import router as health_router
from core.llm_client import simple_completion
from dotenv import load_dotenv
load_dotenv()
app = FastAPI(
    title="Agentic Workflow Automator",
    description="Backend for an agentic AI system",
    version="0.1.0"
)

app.include_router(health_router, prefix="/api/health")

@app.get("/")
def root():
    return {"message": "Backend running"}


@app.get("/api/llm-test")
def llm_test():
    return {
        "response": simple_completion(
            "Explain what an AI agent is in one sentence."
        )
    }
