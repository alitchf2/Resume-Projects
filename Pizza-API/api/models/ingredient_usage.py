from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class IngredientUsage(Base):
    __tablename__ = 'ingredient_usage'
    id = Column(Integer, primary_key=True)
    pizza_id = Column(Integer, ForeignKey('pizza.id'))
    ingredient_id = Column(Integer , ForeignKey('ingredients.id'))
    quantity = Column(Integer)

    ingredient = relationship('Ingredient', back_populates='ingredient_usage')
    pizza = relationship('Pizza', back_populates='ingredient_usage')
