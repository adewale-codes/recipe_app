from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

recipe_ingredient = Table(
    'recipe_ingredient',
    Base.metadata,
    Column('recipe_id', Integer, ForeignKey('recipes.id'), primary_key=True),
    Column('ingredient_id', Integer, ForeignKey('ingredients.id'), primary_key=True)
)

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, index=True)
    cuisine = Column(String, index=True)

    ingredients = relationship('Ingredient', secondary=recipe_ingredient, back_populates='recipes')

class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    recipes = relationship('Recipe', secondary=recipe_ingredient, back_populates='ingredients')
