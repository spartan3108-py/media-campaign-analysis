from fastapi import FastAPI
from src.routers import campaign_router

app = FastAPI(
    title="Media Campaign Analysis API",
    version="1.0.0",
)

app.include_router(campaign_router)


@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint."""
    return {"message": "Service is healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="0.0.0.0", port=5002, reload=True)
