from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import customers as model
from sqlalchemy.exc import SQLAlchemyError
from ..schemas.customers import CustomerCreate, CustomerUpdate

def create(db: Session, request: CustomerCreate):
    # Create a new customer in the database
    new_customer = model.Customer(
        name=request.name,
        email=request.email,
        phone=request.phone,
        address=request.address
    )

    try:
        db.add(new_customer)
        db.commit()
        db.refresh(new_customer)
    except SQLAlchemyError as e:
        _handle_db_error(e)
    return new_customer


def read_all(db: Session):
    # Retrieve all customers from database
    try:
        return db.query(model.Customer).all()
    except SQLAlchemyError as e:
        _handle_db_error(e)


def read_one(db: Session, customer_id: int):
    # Retrieve a single customer by ID
    try:
        customer = db.query(model.Customer).filter(model.Customer.id == customer_id).first()
        if not customer:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer is not found")
    except SQLAlchemyError as e:
        _handle_db_error(e)
    return customer

def update(db: Session, customer_id: int, request: CustomerUpdate):
    # Update an existing customer's details
    try:
        customer = db.query(model.Customer).filter(model.Customer.id == customer_id)
        if not customer:
             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer is not found")
        update_data = request.dict(exclude_unset=True)
        customer.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        _handle_db_error(e)
    return customer.first()

def delete(db: Session, customer_id: int):
    # Delete a customer by ID
    try:
        customer = db.query(model.Customer).filter(model.Customer.id == customer_id)
        if not customer.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer IS not found")
        customer.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        _handle_db_error(e)
    return True

def _handle_db_error(e: SQLAlchemyError):
    # Utility function to handle database errors
    error = str(e.__dict__['orig'])
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)