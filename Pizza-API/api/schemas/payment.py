from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PaymentBase(BaseModel):
    payment_type: str
    card_info: str

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(PaymentBase):
    pass

class Payment(PaymentBase):
    id: int

    class ConfigDict:
        from_attributes = True