from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Pizza(Base):
    __tablename__ = 'pizza'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50))
    price = Column(DECIMAL)
    calories = Column(DECIMAL)
    category = Column(String(30))

    order_details = relationship("OrderDetail", back_populates="pizza")
    ingredient_usage = relationship("IngredientUsage", back_populates="pizza")
    review = relationship("Review", back_populates="pizza")
