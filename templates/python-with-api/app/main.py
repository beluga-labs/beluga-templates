from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from app.core.limiter import limiter
from app.core.logger import logger
from app.routers import token, user


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application startup")
    yield
    logger.info("Application shutdown")


app = FastAPI(lifespan=lifespan, title="beluga labs API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.include_router(user.router)
app.include_router(token.router)


@app.get("/")
def root():
    logger.info("Root endpoint was called")
    return {"message": "Welcome to a beluga labs application!"}
