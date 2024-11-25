import pytest
from src.repositories.user_repository import UserRepository

def test_repository():
    repository = UserRepository()

    # Crear usuario
    repository.create_user("1", "Tony")
    assert repository.get_user_by_id("1") == {"id": "1", "name": "Tony"}

    # Leer usuario
    assert repository.get_user_by_id("1") is not None

    # Actualizar usuario
    repository.update_user("1", "Tony")
    assert repository.get_user_by_id("1") == {"id": "1", "name": "Tony"}

    # Eliminar usuario
    repository.delete_user("1")
    assert repository.get_user_by_id("1") is None
