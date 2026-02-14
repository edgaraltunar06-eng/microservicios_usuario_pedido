from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.user_model import User, UserUpdate

class UserRepositoryPort(ABC):
    @abstractmethod
    def create(self, user: User) -> User:
        pass
    @abstractmethod
    def get_all(self) -> List[User]:
        pass
    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]:
        pass
    @abstractmethod
    def update(self, user_id: int, user_data: UserUpdate) -> Optional[User]:
        pass
    @abstractmethod
    def delete(self, user_id: int) -> bool:
        pass