from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import List

"""
This module implements a simple chat functionality using WebSockets.

It defines a ConnectionManager class to handle WebSocket connections
and provides a router for the chat endpoint.
"""

router = APIRouter()


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


# Create an instance of ConnectionManager
# This manager will handle WebSocket connections for the chat
# It keeps track of active connections and broadcasts messages to all connected clients
manager = ConnectionManager()


@router.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # This line broadcasts the received message to all connected clients
            # It uses an f-string to format the message, prefixing it with "Message: "
            # The 'data' variable contains the text received from the client
            # The 'manager.broadcast' method sends this formatted message to all active connections
            await manager.broadcast(f"Message: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast("A user has left the chat")
