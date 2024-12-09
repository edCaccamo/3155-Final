from typing import Optional, List, Annotated
from pydantic import BaseModel, condecimal

#for formatting price
ConDecimal4_2 = Annotated[float, condecimal(max_digits=4, decimal_places=2)]


class SandwichBase(BaseModel):
    sandwich_name: Optional[str] = None
    price: ConDecimal4_2 = 0.00
    ingrediants: Optional[str] = None
    calories: ConDecimal4_2 = 0.00
    category: Optional[str] = None

class SandwichCreate(SandwichBase):
    sandwich_name: str
    price: ConDecimal4_2 = 0.00

class SandwichUpdate(BaseModel):
    sandwich_name: Optional[str] = None
    price: Optional[ConDecimal4_2] = None
    ingrediants: Optional[str] = None
    calories: Optional[ConDecimal4_2] = None
    category: Optional[str] = None

class Sandwich(SandwichBase):
    id: int

    class ConfigDict:
        from_attributes = True
