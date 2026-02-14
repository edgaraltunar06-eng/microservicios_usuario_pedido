from fastapi import APIRouter, HTTPException, status
from src.domain.user_model import User, UserUpdate
from src.application.services.user_service import UserService
from src.infrastructure.adapters.in_memory_repository import InMemoryUserRepository

router = APIRouter()

repo = InMemoryUserRepository()
service = UserService(repo)

@router.post("/users/", status_code=status.HTTP_201_CREATED, response_model=User)
def create_user(user: User):
    existing = service.get_user(user.id_usuario)
    if existing:
        raise HTTPException(status_code=400, detail="User ID already exists")
    return service.create_user(user)

@router.get("/users/", response_model=list[User])
def read_users():
    return service.get_users()

@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    user = service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user_data: UserUpdate):
    updated_user = service.update_user(user_id, user_data)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    success = service.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return None