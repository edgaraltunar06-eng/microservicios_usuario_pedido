from fastapi import APIRouter, HTTPException, status
from typing import List
from src.domain.order_model import Order, OrderUpdate
from src.application.services.order_service import OrderService
from src.infrastructure.adapters.in_memory_order_repository import InMemoryOrderRepository

router = APIRouter()

repo = InMemoryOrderRepository()
service = OrderService(repo)

@router.post("/orders/", status_code=status.HTTP_201_CREATED, response_model=Order)
def create_order(order: Order):
    existing = service.get_order(order.id_pedido)
    if existing:
        raise HTTPException(status_code=400, detail="Order ID already exists")
    return service.create_order(order)

@router.get("/orders/", response_model=List[Order])
def read_orders():
    return service.get_orders()

@router.get("/orders/{order_id}", response_model=Order)
def read_order(order_id: int):
    order = service.get_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.put("/orders/{order_id}", response_model=Order)
def update_order(order_id: int, order_data: OrderUpdate):
    updated_order = service.update_order(order_id, order_data)
    if not updated_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return updated_order

@router.delete("/orders/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(order_id: int):
    success = service.delete_order(order_id)
    if not success:
        raise HTTPException(status_code=404, detail="Order not found")
    return None