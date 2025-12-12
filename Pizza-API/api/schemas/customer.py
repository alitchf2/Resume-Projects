from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .orders import OrderBase

class CustomerBase(BaseModel):
    name : Optional[str] = None
    email : Optional[str] = None
    phone : Optional[str] = None
    address : Optional[str] = None

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(BaseModel):
    name : Optional[str] = None
    email : Optional[str] = None
    phone : Optional[str] = None
    address : Optional[str] = None

class Customer(CustomerBase):
    id : int

    class ConfigDict:
        from_attributes = True

