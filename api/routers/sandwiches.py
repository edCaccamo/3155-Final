from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..controllers import sandwiches as controller
from ..schemas import sandwiches as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=["Sandwiches"],
    prefix="/sandwiches"
)

# Create a new sandwich
@router.post("/", response_model=schema.Sandwich)
def create(request: schema.SandwichCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

# Get all sandwiches
@router.get("/", response_model=list[schema.Sandwich])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

# Get a single sandwich by ID
@router.get("/{sandwich_id}", response_model=schema.Sandwich)
def read_one(sandwich_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db=db, sandwich_id=sandwich_id)

# Update a sandwich by ID
@router.put("/{sandwich_id}", response_model=schema.Sandwich)
def update(sandwich_id: int, request: schema.SandwichUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, sandwich_id=sandwich_id, request=request)

# Delete a sandwich by ID
@router.delete("/{sandwich_id}")
def delete(sandwich_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, sandwich_id=sandwich_id)
