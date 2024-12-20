from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base
from .associations import recipe_resource_table


class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    item = Column(String(300), unique=True, nullable=False)
    amount = Column(Integer, index=True, nullable=False, server_default='0.0')
    unit = Column(String(100), nullable=True)

    recipes = relationship("Recipe", secondary=recipe_resource_table, back_populates="resources")