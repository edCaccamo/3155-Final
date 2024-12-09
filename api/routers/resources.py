from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..controllers import resources as controller
from ..schemas import resources as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=["Resources"],
    prefix="/resources"
)

# Create a new resource
@router.post("/", response_model=schema.Resource)
def create(request: schema.ResourceCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

# Get all resources
@router.get("/", response_model=list[schema.Resource])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

# Get a single resource by ID
@router.get("/{resource_id}", response_model=schema.Resource)
def read_one(resource_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db=db, resource_id=resource_id)

# Update a resource by ID
@router.put("/{resource_id}", response_model=schema.Resource)
def update(resource_id: int, request: schema.ResourceUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, resource_id=resource_id, request=request)

# Delete a resource by ID
@router.delete("/{resource_id}")
def delete(resource_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, resource_id=resource_id)
