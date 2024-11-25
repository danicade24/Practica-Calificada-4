import pytest
from fastapi.testclient import TestClient
from src.main import app

# Fixture para crear un cliente de prueba
@pytest.fixture
def client():
    return TestClient(app)

def test_create_user(client):
    # Crear un usuario
    response = client.post("/users", json={"user_id": "1", "name": "Tony"})
    assert response.status_code == 200
    assert response.json() == {"user": {"id": "1", "name": "Tony"}}

def test_get_user(client):
    # Crear un usuario
    client.post("/users", json={"user_id": "1", "name": "Tony"})

    # Obtener usuario por ID
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"user": {"id": "1", "name": "Tony"}}

def test_list_users(client):
    # Crear un usuario
    client.post("/users", json={"user_id": "1", "name": "Tony"})

    # Listar todos los usuarios
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == {"users": {"1": {"id": "1", "name": "Tony"}}}

def test_delete_user(client):
    # Crear un usuario
    client.post("/users", json={"user_id": "1", "name": "Tony"})

    # Eliminar el usuario
    response = client.delete("/users/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Usuario eliminado"}

    # Intentar obtener un usuario eliminado
    response = client.get("/users/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Usuario no encontrado"}

def test_list_users_empty(client):
    # Listar usuarios cuando no hay ninguno
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == {"users": {}}


def test_update_user_success(client):
    # Crear un usuario
    client.post("/users", json={"user_id": "1", "name": "Tony"})

    # Actualizar el usuario
    response = client.put("/users/1", json={"user_id": "1", "name": "Tony"})
    assert response.status_code == 200
    assert response.json() == {"user": {"id": "1", "name": "Tony"}}

def test_update_user_not_found(client):
    # Intentar actualizar un usuario que no existe
    response = client.put("/users/999", json={"user_id": "999", "name": "New Name"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Usuario no encontrado"}

def test_update_user_invalid_body(client):
    # Crear un usuario
    client.post("/users", json={"user_id": "1", "name": "Tony"})

    # Intentar actualizar con un cuerpo vacío
    response = client.put("/users/1", json={})
    assert response.status_code == 422  # Unprocessable Entity

    # Intentar actualizar con un cuerpo incompleto (sin `name`)
    response = client.put("/users/1", json={"user_id": "1"})
    assert response.status_code == 422  # Unprocessable Entity
