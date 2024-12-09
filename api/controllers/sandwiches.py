from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from ..models.sandwiches import Sandwich
from ..schemas.sandwiches import SandwichCreate, SandwichUpdate


def create(db: Session, request: SandwichCreate):
    # Create a new sandwich
    new_sandwich = Sandwich(
        sandwich_name=request.sandwich_name,
        price=request.price,
        ingrediants=request.ingrediants,
        calories=request.calories,
        category=request.category
    )

    try:
        db.add(new_sandwich)
        db.commit()
        db.refresh(new_sandwich)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_sandwich


def read_all(db: Session):
    # Retrieve all sandwiches from database
    try:
        return db.query(Sandwich).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def read_one(db: Session, sandwich_id: int):
    # Retrieve a sandwich by ID from database
    sandwich = db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()
    if not sandwich:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sandwich not found")
    return sandwich


def update(db: Session, sandwich_id: int, request: SandwichUpdate):
    # Update a sandwich's data 
    sandwich = db.query(Sandwich).filter(Sandwich.id == sandwich_id)
    if not sandwich.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sandwich not found")

    try:
        update_data = request.dict(exclude_unset=True)
        sandwich.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return sandwich.first()


def delete(db: Session, sandwich_id: int):
    # Delete a sandwich by ID
    sandwich = db.query(Sandwich).filter(Sandwich.id == sandwich_id)
    if not sandwich.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sandwich not found")

    try:
        sandwich.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return True
