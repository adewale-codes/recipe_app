from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from services.recommender import recommend

router = APIRouter()

class RecommendRequest(BaseModel):
    ingredients: List[str]

class RecipeOut(BaseModel):
    id: int
    cuisine: Optional[str]
    ingredients: List[str]

@router.post("/", response_model=List[RecipeOut])
async def recommend_recipes(body: RecommendRequest):
    recs = recommend(body.ingredients)
    if not recs:
        raise HTTPException(status_code=404, detail="No matching recipes found.")
    return recs