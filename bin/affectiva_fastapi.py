from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory "database"
affectiva_db = []

# Pydantic model
class Affectiva(BaseModel):
    joy: float
    sadness: float
    disgust: float
    contempt: float
    anger: float
    fear: float
    surprise: float
    valence: float
    engagement: float
    Timestamp: float
    smile: float
    innerBrowRaise: float
    browRaise: float
    browFurrow: float
    noseWrinkle: float
    upperLipRaise: float
    lipCornerDepressor: float
    chinRaise: float
    lipPucker: float
    lipPress: float
    lipSuck: float
    mouthOpen: float
    smirk: float
    eyeClosure: float
    attention: float
    lidTighten: float
    jawDrop: float
    dimpler: float
    eyeWiden: float
    cheekRaise: float
    lipStretch: float

@app.get("/")
def index():
    return {"message": "Affectiva FastAPI is running"}

@app.get("/affectiva/")
def get_all():
    return affectiva_db

@app.get("/affectiva/{entry_id}/")
def get_one(entry_id: int = Path(..., gt=0)):
    return affectiva_db[entry_id - 1]

@app.post("/affectiva/")
def add_one(entry: Affectiva):
    affectiva_db.append(entry.model_dump())
    return affectiva_db[-1]

@app.post("/affectiva/bulk/")
def add_many(entries: List[Affectiva]):
    for entry in entries:
        affectiva_db.append(entry.model_dump())
    return {"added": len(entries)}

@app.delete("/affectiva/{entry_id}/")
def delete_one(entry_id: int = Path(..., gt=0)):
    affectiva_db.pop(entry_id - 1)
    return {"message": f"Entry {entry_id} deleted"}
