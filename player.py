from pydantic import BaseModel

class PlayerCreate(BaseModel):
    name: str
    team: str
    points: float
    rebounds: float
    assists: float

class Player(PlayerCreate):
    id: str

    



