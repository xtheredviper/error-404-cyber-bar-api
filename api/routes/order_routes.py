from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.models.order_models import OrderCreate, OrderStatus

from api.services.order_service import (
    create_new_order,
    get_all_orders,
    update_status
)

from api.database.connection import get_db


router = APIRouter()


@router.post("/order")
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db)
):
    return create_new_order(order, db)


@router.get("/orders")
def get_orders(
    db: Session = Depends(get_db)
):
    return get_all_orders(db)


@router.patch("/orders/{order_id}")
def update_order(
    order_id: int,
    updated_status: OrderStatus,
    db: Session = Depends(get_db)
):
    return update_status(order_id, updated_status, db)