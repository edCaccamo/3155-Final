from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from ..models.recipes import Recipe
from ..schemas.recipes import RecipeCreate, RecipeUpdate


def create(db: Session, request: RecipeCreate):
    # Create a new recipe
    new_recipe = Recipe(
        sandwich_id=request.sandwich_id,
        resource_id=request.resource_id,
        amount=request.amount
    )

    try:
        db.add(new_recipe)
        db.commit()
        db.refresh(new_recipe)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_recipe


def read_all(db: Session):
    # Retrieve all recipies from database
    try:
        return db.query(Recipe).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def read_one(db: Session, recipe_id: int):
    # Retrieve a recipe based on ID from database
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found")
    return recipe


def update(db: Session, recipe_id: int, request: RecipeUpdate):
    # Update an existing recipe's details
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id)
    if not recipe.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found")

    try:
        update_data = request.dict(exclude_unset=True)
        recipe.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return recipe.first()


def delete(db: Session, recipe_id: int):
    # Delete a existing recipie
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id)
    if not recipe.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recipe not found")

    try:
        recipe.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return True
