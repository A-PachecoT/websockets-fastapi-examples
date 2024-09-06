from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.chat import router as chat_router
from app.data_stream import router as data_stream_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(chat_router)
app.include_router(data_stream_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
