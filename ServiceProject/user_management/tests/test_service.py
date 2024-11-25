from src.services.user_service import UserService

class MockRepository:
    def __init__(self):
        self.users = {}

    def get_all_users(self):
        return self.users

    def get_user_by_id(self, user_id: str):
        return self.users.get(user_id)

    def create_user(self, user_id: str, name: str):
        self.users[user_id] = {"id": user_id, "name": name}
        return self.users[user_id]

    def update_user(self, user_id: str, name: str):
        if user_id in self.users:
            self.users[user_id]["name"] = name
            return self.users[user_id]
        return None

    def delete_user(self, user_id: str):
        return self.users.pop(user_id, None)

def test_service():
    mock_repo = MockRepository()
    service = UserService(mock_repo)

    # Crear usuario
    service.create_user("1", "Tony")
    assert mock_repo.get_user_by_id("1") == {"id": "1", "name": "Tony"}

    # Leer usuarios
    assert service.get_users() == {"1": {"id": "1", "name": "Tony"}}

    # Actualizar usuario
    service.update_user("1", "Tony")
    assert mock_repo.get_user_by_id("1") == {"id": "1", "name": "Tony"}

    # Eliminar usuario
    service.delete_user("1")
    assert mock_repo.get_user_by_id("1") is None
