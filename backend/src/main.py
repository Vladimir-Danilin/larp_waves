from contextlib import asynccontextmanager

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Application is starting...")

    # Например:
    # await database.connect()
    # await redis.connect()

    yield

    # Shutdown
    print("Application is shutting down...")

    # Например:
    # await database.disconnect()
    # await redis.disconnect()


app = FastAPI(
    title="My API",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/health", tags=["Health"])
async def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )