from fastapi import FastAPI, Request
from app.proxy.middleware import risk_gate_middleware

app = FastAPI()
app.middleware("http")(risk_gate_middleware)

@app.get("/health")
async def health():
    return {"status": "ok"}