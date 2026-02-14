from typing import List, Optional
from src.domain.order_model import Order, OrderUpdate
from src.application.ports.order_repository import OrderRepositoryPort

class InMemoryOrderRepository(OrderRepositoryPort):
    def __init__(self):
        self.db: List[Order] = []

    def create(self, order: Order) -> Order:
        self.db.append(order)
        return order

    def get_all(self) -> List[Order]:
        return self.db

    def get_by_id(self, order_id: int) -> Optional[Order]:
        return next((o for o in self.db if o.id_pedido == order_id), None)

    def update(self, order_id: int, order_data: OrderUpdate) -> Optional[Order]:
        order = self.get_by_id(order_id)
        if order:
            if order_data.items:
                order.items = order_data.items
            if order_data.total is not None:
                order.total = order_data.total
            if order_data.estado:
                order.estado = order_data.estado
            return order
        return None

    def delete(self, order_id: int) -> bool:
        order = self.get_by_id(order_id)
        if order:
            self.db.remove(order)
            return True
        return False