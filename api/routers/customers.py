from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import customers as controller
from ..schemas import customers as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=["Customers"],
    prefix="/customers"
)

# Create a new custoemr
@router.post("/", response_model=schema.Customer, status_code=status.HTTP_201_CREATED)
def create_customer(request: schema.CustomerCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

# Get all customers
@router.get("/", response_model=list[schema.Customer], status_code=status.HTTP_200_OK)
def read_all_customers(db: Session = Depends(get_db)):
    return controller.read_all(db=db)

# Get a single customer by ID
@router.get("/{customer_id}", response_model=schema.Customer, status_code=status.HTTP_200_OK)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db=db, customer_id=customer_id)

# Update a customer by ID
@router.put("/{customer_id}", response_model=schema.Customer, status_code=status.HTTP_200_OK)
def update_customer(customer_id: int, request: schema.CustomerUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, customer_id=customer_id, request=request)

# Delete a customer by ID
@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    success = controller.delete(db=db, customer_id=customer_id)
    if success:
        return Response(status_code=status.HTTP_204_NO_CONTENT)