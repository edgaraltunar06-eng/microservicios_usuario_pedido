from typing import List, Optional
from src.domain.user_model import User, UserUpdate
from src.application.ports.user_repository import UserRepositoryPort

class InMemoryUserRepository(UserRepositoryPort):
    def __init__(self):
        self.db: List[User] = []

    def create(self, user: User) -> User:
        self.db.append(user)
        return user

    def get_all(self) -> List[User]:
        return self.db

    def get_by_id(self, user_id: int) -> Optional[User]:
        return next((u for u in self.db if u.id_usuario == user_id), None)

    def update(self, user_id: int, user_data: UserUpdate) -> Optional[User]:
        user = self.get_by_id(user_id)
        if user:
            if user_data.nombre:
                user.nombre = user_data.nombre
            if user_data.email:
                user.email = user_data.email
            return user
        return None

    def delete(self, user_id: int) -> bool:
        user = self.get_by_id(user_id)
        if user:
            self.db.remove(user)
            return True
        return False