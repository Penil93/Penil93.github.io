from fastapi import Body, FastAPI, APIRouter
import uvicorn
from pydantic import BaseModel

import os, json

import time

router = APIRouter(prefix = '/api')
app = FastAPI(
    title = "Chang Won's Blog Back-end Server",
    version = "0.1"
)

@router.post('/ping')
async def blog_ping():
    return {"code": 200, "result": "Pong"}

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("__main__:app", host = "0.0.0.0", port = 1993)