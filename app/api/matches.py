from slowapi.util import get_remote_address
from slowapi import Limiter
from fastapi import APIRouter, Request, Response, Depends

from app.core.dependencies import limiter
from app.models.match import MatchResponse

router = APIRouter()


@router.get("/recent", response_model=list[MatchResponse])
@limiter.limit("3/second")
async def get_recent_matches(request: Request, response: Response):
    matches = [
        MatchResponse(match_id=123, team_1="SEN", team_2="LOUD", status="finished"),
    ]
    return matches
