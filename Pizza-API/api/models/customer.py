from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50))
    email = Column(String(50))
    phone = Column(String(20))
    address = Column(String(100))

    order = relationship("Order", back_populates="customer")