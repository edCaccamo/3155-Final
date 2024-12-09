from sqlalchemy import Column, Table, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base
from . import resources
from .associations import recipe_resource_table

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))

    sandwich = relationship("Sandwich", back_populates="recipes")
    resources = relationship("Resource", secondary=recipe_resource_table, back_populates="recipes")