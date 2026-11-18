from contextlib import asynccontextmanager
from pathlib import Path

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from business.errors import BusinessError, NotFoundError
from persistence.database import SessionLocal, init_db
from persistence.db_entries import insert_db_entries
from service import game_endpoints, player_endpoints


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    with SessionLocal() as session:
        insert_db_entries(session)
    yield


async def business_error_handler(request: Request, error: BusinessError):
    status_code = 404 if isinstance(error, NotFoundError) else 400
    return JSONResponse(status_code=status_code, content={"error": str(error)})


app = FastAPI(title="KickerRank", lifespan=lifespan)
app.add_exception_handler(BusinessError, business_error_handler)
app.include_router(player_endpoints.router)
app.include_router(game_endpoints.router)
app.mount("/", StaticFiles(directory=Path(__file__).parent / "presentation", html=True), name="presentation")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
