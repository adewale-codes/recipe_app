import json
import os
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from db.database import SessionLocal, init_db, engine
from db.models import Base, Recipe, Ingredient


def seed_data():
    Base.metadata.drop_all(bind=engine)
    init_db()

    db: Session = SessionLocal()

    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    data_path = os.path.join(base_dir, 'data', 'train.json')

    with open(data_path, 'r', encoding='utf-8') as f:
        recipes_list = json.load(f)

    for rec in recipes_list:
        recipe = db.merge(Recipe(id=rec['id'], cuisine=rec.get('cuisine')))

        for ing_name in rec.get('ingredients', []):
            name_clean = ing_name.strip().lower()
            ing = db.query(Ingredient).filter_by(name=name_clean).first()
            if not ing:
                ing = Ingredient(name=name_clean)
                db.add(ing)
                db.flush()

            if ing not in recipe.ingredients:
                recipe.ingredients.append(ing)

        try:
            db.commit()
        except IntegrityError:
            db.rollback()

    db.close()


if __name__ == "__main__":
    seed_data()
    print("Seeded database with recipes and ingredients.")