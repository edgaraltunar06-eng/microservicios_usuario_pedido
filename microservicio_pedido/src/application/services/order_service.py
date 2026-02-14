from typing import List, Optional
from src.domain.order_model import Order, OrderUpdate
from src.application.ports.order_repository import OrderRepositoryPort

class OrderService:
    def __init__(self, repository: OrderRepositoryPort):
        self.repository = repository

    def create_order(self, order: Order) -> Order:
        return self.repository.create(order)

    def get_orders(self) -> List[Order]:
        return self.repository.get_all()

    def get_order(self, order_id: int) -> Optional[Order]:
        return self.repository.get_by_id(order_id)

    def update_order(self, order_id: int, order_data: OrderUpdate) -> Optional[Order]:
        return self.repository.update(order_id, order_data)

    def delete_order(self, order_id: int) -> bool:
        return self.repository.delete(order_id)