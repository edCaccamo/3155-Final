from typing import Optional, List
from pydantic import BaseModel, EmailStr

class CustomerBase(BaseModel):
    name: str
    email: EmailStr
    phone: str
    address: Optional[str]

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class Customer(CustomerBase):
    id: int

    class Config:
        from_attributes = True
