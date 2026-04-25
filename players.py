from fastapi import APIRouter, HTTPException, Depends, status
from models.player import Player, PlayerCreate
from models.auth import get_current_user
import uuid
from backend.database import players_collection
router = APIRouter(prefix = "/players", tags = ["players"])



def to_player(doc) -> Player:
    return Player(id = doc["_id"], name = doc["name"], team = doc["team"], points = doc["points"], rebounds = doc["rebounds"], assists=doc["assists"])


@router.get("/")
async def get_players():
    players = await players_collection.find().to_list(100)
    return players


@router.post("/", response_model = Player, status_code = status.HTTP_201_CREATED)
async def create_player(player: PlayerCreate, current_user: str = Depends(get_current_user)):
    new_id = str(uuid.uuid4())

    doc = {"_id": new_id, **player.dict()}

    await players_collection.insert_one(doc)
    return to_player(doc)

@router.put("/{player_id}", response_model=Player)
async def update_player(player_id:str, player: PlayerCreate, current_user: str = Depends(get_current_user)):
    update = {"$set": player.dict()}
    result = await players_collection.update_one({"_id": player_id}, update)
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Player not found")
    doc = await players_collection.find_one({"_id": player_id})
    return to_player(doc)

@router.delete("/{player_id}")
async def delete_player(player_id: str, current_user: str = Depends(get_current_user)):
    result = await players_collection.delete_one({"_id": player_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Player not found")
    return {"msg": "Player deleted"}