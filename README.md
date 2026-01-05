# Adaptive API Risk Gate

An async, behavior-aware traffic control system that dynamically reshapes API traffic
based on real-time risk signals to prevent cascading failures during partial outages.

## Why this project?
Traditional rate limiters and API gateways rely on static thresholds.
This system adapts traffic decisions based on:
- Behavioral anomalies
- Downstream latency & error rates
- System saturation

This is an **internal-infra style prototype**, inspired by MAANG-scale systems.

## Architecture
- FastAPI + asyncio (async reverse proxy)
- Redis for distributed state
- Adaptive token bucket
- Risk scoring engine

## How to run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
