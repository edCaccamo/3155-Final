from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import recipes as model, resources as resource_model
from ..schemas import recipes as schema
from sqlalchemy.exc import SQLAlchemyError
from ..models.associations import recipe_resource_table
from sqlalchemy import select, insert, delete as sa_delete
from ..schemas.recipes import RecipeUpdate
from ..models.recipes import Recipe


def create(db: Session, request: schema.RecipeCreate):
    # initial creaction
    new_recipe = model.Recipe(sandwich_id=request.sandwich_id)
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)

    #add resources to association table
    for item in request.resources:
        resource_id = item.resource_id
        amount = item.amount

        # Checks if resource is real
        resource = db.query(resource_model.Resource).filter_by(id=resource_id).first()
        if not resource:
            raise HTTPException(status_code=404, detail=f"Resource with ID {resource_id} not found")

        #Insert
        db.execute(recipe_resource_table.insert().values(
            recipe_id=new_recipe.id,
            resource_id=resource_id,
            amount=amount
        ))

    db.commit()
    return new_recipe


def read_all(db: Session):
    try:
        result = db.query(model.Recipe).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.Recipe).filter(model.Recipe.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id: int, request: RecipeUpdate):
    try:
        # Check recipe exists
        recipe = db.query(Recipe).filter(Recipe.id == item_id).first()
        if not recipe:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found!")

        # Update sandwich_id
        if request.sandwich_id is not None:
            recipe.sandwich_id = request.sandwich_id

        # Update resources
        if request.resources is not None:
            db.execute(sa_delete(recipe_resource_table).where(recipe_resource_table.c.recipe_id == item_id))

            new_resources = [
                {"recipe_id": item_id, "resource_id": res.resource_id, "amount": res.amount}
                for res in request.resources
            ]
            db.execute(insert(recipe_resource_table), new_resources)

        db.commit()
        db.refresh(recipe)

        return recipe

    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def delete(db: Session, item_id):
    try:
        item = db.query(model.Recipe).filter(model.Recipe.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def get_resources_by_recipe_id(db: Session, recipe_id: int):
    try:
        stmt = select(
            recipe_resource_table.c.resource_id,
            recipe_resource_table.c.amount
        ).where(recipe_resource_table.c.recipe_id == recipe_id)
        results = db.execute(stmt).fetchall()

        if not results:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        
        return [{"resource_id": row.resource_id, "amount": row.amount} for row in results]

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))