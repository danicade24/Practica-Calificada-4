from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.services.user_service import UserService
from src.repositories.user_repository import UserRepository

router = APIRouter()

repository = UserRepository()
service = UserService(repository)

# Modelo de datos para la creación y actualización de usuarios
class User(BaseModel):
    user_id: str
    name: str

@router.get("/users")
def get_users():
    return {"users": service.get_users()}

@router.get("/users/{user_id}")
def get_user(user_id: str):
    try:
        return {"user": service.get_user(user_id)}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/users")
def create_user(user: User):
    try:
        return {"user": service.create_user(user.user_id, user.name)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/users/{user_id}")
def update_user(user_id: str, user: User):
    try:
        return {"user": service.update_user(user_id, user.name)}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.delete("/users/{user_id}")
def delete_user(user_id: str):
    try:
        service.delete_user(user_id)  # Asumimos que devuelve `None` al eliminar correctamente
        return {"message": "Usuario eliminado"}  # Devuelve el mensaje fijo
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

