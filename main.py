from fastapi import FastAPI
from pydantic import BaseModel

from archetype_prediction import predict_character_archetype

app = FastAPI()

class UserCharacterDescription(BaseModel):
    description: str

@app.post("/getArchetypePrediction/")
async def create_item(item: UserCharacterDescription):
    return {"embedding": predict_character_archetype(item.description).tolist()}