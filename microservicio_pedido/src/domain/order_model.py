from pydantic import BaseModel
from typing import Optional

class Order(BaseModel):
    id_pedido: int
    id_usuario: int
    items: str
    total: float
    estado: str = "Pendiente"

class OrderUpdate(BaseModel):
    items: Optional[str] = None
    total: Optional[float] = None
    estado: Optional[str] = None