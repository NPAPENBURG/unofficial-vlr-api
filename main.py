from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from fastapi import FastAPI, Request
from slowapi.errors import RateLimitExceeded


from app.api.router import api_router
from app.core.dependencies import limiter

app = FastAPI(
    title="Valorant VLR.gg Scraper API",
    description="Live-scraped Valorant data from VLR.gg for matches, players, and teams.",
    version="0.1.0",
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Include all your API routes
app.include_router(api_router)

# Optional startup/shutdown events
@app.on_event("startup")
async def startup_event():
    print("Starting up...")

@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down...")
