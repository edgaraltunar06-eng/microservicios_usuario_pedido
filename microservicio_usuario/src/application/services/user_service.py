from typing import List, Optional
from src.domain.user_model import User, UserUpdate
from src.application.ports.user_repository import UserRepositoryPort

class UserService:
    def __init__(self, repository: UserRepositoryPort):
        self.repository = repository

    def create_user(self, user: User) -> User:
        return self.repository.create(user)

    def get_users(self) -> List[User]:
        return self.repository.get_all()

    def get_user(self, user_id: int) -> Optional[User]:
        return self.repository.get_by_id(user_id)

    def update_user(self, user_id: int, user_data: UserUpdate) -> Optional[User]:
        return self.repository.update(user_id, user_data)

    def delete_user(self, user_id: int) -> bool:
        return self.repository.delete(user_id)