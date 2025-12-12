from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    status = Column(Enum("pending", "paid", "complete", name="order_status"), default="pending")
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    total_price = Column(DECIMAL)
    promo_id = Column(Integer, ForeignKey('promos.id'), nullable=True)
    delivery = Column(Boolean)
    payment_id = Column(Integer, ForeignKey('payment.id'), nullable=True)

    customer = relationship("Customer", back_populates="order")
    order_details = relationship("OrderDetail", back_populates="order")
    promo = relationship("Promo", back_populates="order")
    payment = relationship("Payment", back_populates="order")