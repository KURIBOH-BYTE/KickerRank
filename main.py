from contextlib import asynccontextmanager
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from persistence.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="KickerRank", lifespan=lifespan)
app.mount("/", StaticFiles(directory=Path(__file__).parent / "presentation", html=True), name="presentation")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
