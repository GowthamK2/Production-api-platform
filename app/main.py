from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi import HTTPException

from app.exception_handlers import (
    http_exception_handler
)

import time
import logging

from app.routers.products import router as product_router
from app.routers.auth import router as auth_router

logging.basicConfig(
level=logging.INFO
)

logger = logging.getLogger(__name__)

app = FastAPI()

app.add_exception_handler(
    HTTPException,
    http_exception_handler
)

@app.middleware("http")
async def log_requests(request, call_next):
    start_time = time.time()
    response = await call_next(request)

    process_time = time.time() - start_time

    logger.info(
        f"{request.method} {request.url.path} "
        f"took {process_time:.4f} seconds"
    )
    return response


app.add_middleware(
CORSMiddleware,
allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"]
)

@app.get("/")
async def home():
    return {
        "message": "Production API Platform Running"
    }

app.include_router(product_router)
app.include_router(auth_router)
