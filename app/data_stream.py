from fastapi import APIRouter, WebSocket
import asyncio
import random

router = APIRouter()


@router.websocket("/ws/data")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = {
                "temperature": round(random.uniform(20, 30), 2),
                "humidity": round(random.uniform(30, 70), 2),
            }
            await websocket.send_json(data)
            await asyncio.sleep(1)
    except Exception:
        await websocket.close()
