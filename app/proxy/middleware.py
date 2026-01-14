import time
from app.risk_engine.scorer import compute_risk
from app.policy.decision import decide_action
from app.throttling.adaptive_bucket import apply_throttle

async def risk_gate_middleware(request, call_next):
    start = time.time()

    risk = await compute_risk(request)
    decision = decide_action(risk)

    await apply_throttle(decision)

    response = await call_next(request)
    latency = time.time() - start

    response.headers["X-Risk-Score"] = str(round(risk, 2))
    response.headers["X-Latency"] = str(round(latency, 4))
    return response
