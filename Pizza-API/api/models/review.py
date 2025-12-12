from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    rating = Column(Integer)
    text = Column(String(1000))
    pizza_id = Column(ForeignKey('pizza.id'))


    pizza = relationship('Pizza', back_populates='review')
