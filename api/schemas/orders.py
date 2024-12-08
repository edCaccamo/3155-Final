from datetime import datetime
from typing import Optional, List, Annotated
from pydantic import BaseModel, condecimal
from .order_details import OrderDetail
from .promotions import Promotion
from .customers import Customer
from .payment_info import PaymentInfo

#for formatting price
ConDecimal4_2 = Annotated[float, condecimal(max_digits=4, decimal_places=2)]

class OrderBase(BaseModel):
    status: Optional[str] = None
    total_price: Optional[ConDecimal4_2] = None
    customer_id: Optional[int] = None
    promotion_id: Optional[int] = None


class OrderCreate(OrderBase):
    customer_id: int
    status: str
    total_price: ConDecimal4_2 = 0.00


class OrderUpdate(BaseModel):
    status: Optional[str] = None
    total_price: Optional[ConDecimal4_2] = None
    customer_id: Optional[int] = None
    promotion_id: Optional[int] = None


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None
    customer: Optional[Customer] = None
    promotion: Optional[Promotion] = None
    payment_info: Optional[PaymentInfo] = None

    class ConfigDict:
        from_attributes = True