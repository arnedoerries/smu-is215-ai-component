from fastapi import FastAPI
from pydantic import BaseModel

from archetype_prediction import predict_character_archetype

app = FastAPI()

class UserCharacterDescription(BaseModel):
    description: str

@app.post("/items/")
async def create_item(item: UserCharacterDescription):
    return predict_character_archetype(UserCharacterDescription)

