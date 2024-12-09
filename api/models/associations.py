from sqlalchemy import Table, Column, Integer, ForeignKey
from ..dependencies.database import Base

recipe_resource_table = Table(
    "recipe_resources",
    Base.metadata,
    Column("recipe_id", Integer, ForeignKey("recipes.id"), primary_key=True),
    Column("resource_id", Integer, ForeignKey("resources.id"), primary_key=True),
    Column("amount", Integer, nullable=False, server_default='0')
)