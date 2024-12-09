from typing import Optional, List, Dict
from pydantic import BaseModel

class ResourceInput(BaseModel):
    resource_id: int
    amount: int

class RecipeBase(BaseModel):
    sandwich_id: int


class RecipeCreate(RecipeBase):
    resources: List[ResourceInput]

class RecipeUpdate(BaseModel):
    sandwich_id: Optional[int] = None
    resources: Optional[List[ResourceInput]]

class Recipe(RecipeBase):
    id: int

    class ConfigDict:
        from_attributes = True
