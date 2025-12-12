from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = "payment"
    id = Column(Integer, primary_key=True)
    card_info = Column(String(50))
    payment_type = Column(String(30))

    order = relationship("Order", back_populates="payment")