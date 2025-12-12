from datetime import datetime
from typing import Optional, Literal
from pydantic import BaseModel, Field
from .order_details import OrderDetail


class OrderCreateRequest(BaseModel):
    customer_id: int
    delivery: bool

class PayForOrder(BaseModel):
    order_id: int
    payment_id: int

class AddPromoToOrder(BaseModel):
    order_id: int
    promo_code: int

class OrderStatus(BaseModel):
    order_id: int
    status: str

    class ConfigDict:
        from_attributes = True

class OrderBase(BaseModel):
    customer_id: int
    status: str
    order_date: datetime
    total_price: float
    promo_id: Optional[int] = None
    delivery: bool
    payment_id: Optional[int] = None


class OrderCreate(OrderBase):
    pass

class OrderUpdate(OrderBase):
    pass

class OrderUpdateCust(BaseModel):
    customer_id: Optional[int] = None
    delivery: Optional[bool] = None

class OrderUpdateStaff(BaseModel):
    status: Optional[Literal["pending", "paid", "complete"]] = Field(None, description="Order status must be pending, paid, or complete")


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None

    class ConfigDict:
        from_attributes = True
