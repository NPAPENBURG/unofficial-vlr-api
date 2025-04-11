from pydantic import BaseModel


class MatchResponse(BaseModel):
    match_id: int
    team_1: str
    team_2: str
    status: str
