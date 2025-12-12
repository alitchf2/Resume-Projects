from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Ingredient(Base):
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(30))
    amount = Column(DECIMAL)

    ingredient_usage = relationship("IngredientUsage", back_populates="ingredient")
