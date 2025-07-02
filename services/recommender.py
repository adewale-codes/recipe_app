from typing import List, Dict, Any
from sqlalchemy.orm import Session
from db.database import SessionLocal
from db.models import Recipe, Ingredient


def recommend(ingredients: List[str], top_k: int = 10) -> List[Dict[str, Any]]:

    user_ings = {ing.strip().lower() for ing in ingredients}

    db: Session = SessionLocal()
    recipes = db.query(Recipe).all()

    scored = []
    for recipe in recipes:
        recipe_ings = {ing.name for ing in recipe.ingredients}
        score = len(user_ings & recipe_ings)
        if score > 0:
            scored.append((score, recipe))

    scored.sort(key=lambda x: x[0], reverse=True)
    results = []
    for _, recipe in scored[:top_k]:
        results.append({
            "id": recipe.id,
            "cuisine": recipe.cuisine,
            "ingredients": [ing.name for ing in recipe.ingredients]
        })
    db.close()
    return results