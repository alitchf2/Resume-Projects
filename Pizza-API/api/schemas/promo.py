from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from .orders import OrderBase

class PromoBase(BaseModel):
    code : Optional[str] = None
    discount : Optional[int] = None
    expiration_date : Optional[datetime] = None

class PromoCreate(PromoBase):
    pass

class PromoUpdate(BaseModel):
    code : Optional[int] = None
    discount : Optional[int] = None
    expiration_date : Optional[datetime] = None

class Promo(PromoBase):
    id : int
    active: bool = True

    class ConfigDict:
        from_attributes = True
    