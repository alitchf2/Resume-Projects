from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Promo(Base):
    __tablename__ = 'promos'
    id = Column(Integer, primary_key=True)
    code = Column(String(50))
    discount = Column(DECIMAL)
    expiration_date = Column(DATETIME)

    order = relationship("Order", back_populates="promo")



