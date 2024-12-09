from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from ..models.resources import Resource
from ..schemas.resources import ResourceCreate, ResourceUpdate



def create(db: Session, request: ResourceCreate):
    # Create a new resource
    new_resource =Resource(
        item=request.item,
        amount=request.amount,
        unit=request.unit
    )

    try:
        db.add(new_resource)
        db.commit()
        db.refresh(new_resource)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_resource


def read_all(db: Session):
    # Retrieve all resources from database
    try:
        return db.query(Resource).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def read_one(db: Session, resource_id: int):
    # Retrieve a resource by ID from database
    resource = db.query(Resource).filter(Resource.id == resource_id).first()
    if not resource:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
    return resource


def update(db: Session, resource_id: int, request: ResourceUpdate):
    # Update an existing resources details
    resource = db.query(Resource).filter(Resource.id == resource_id)
    if not resource.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")

    try:
        update_data = request.dict(exclude_unset=True)
        resource.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return resource.first()


def delete(db: Session, resource_id: int):
    # Delete a resource by ID
    resource = db.query(Resource).filter(Resource.id == resource_id)
    if not resource.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")

    try:
        resource.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return True
