import random

async def compute_risk(request):
    # Placeholder risk model
    # In real systems this uses sliding windows + EWMA
    base_risk = random.uniform(0.1, 0.4)
    if "retry" in request.headers:
        base_risk += 0.3
    return min(base_risk, 1.0)