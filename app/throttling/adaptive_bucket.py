import asyncio

async def apply_throttle(decision: str):
    if decision == "DELAY":
        await asyncio.sleep(0.05)
    elif decision == "DEGRADE":
        await asyncio.sleep(0.1)
    elif decision == "REJECT":
        await asyncio.sleep(0)
