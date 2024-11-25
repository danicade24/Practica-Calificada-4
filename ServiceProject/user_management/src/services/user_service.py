from repositories.user_repository import UserRepository

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_users(self):
        return self.repository.get_all_users()

    def get_user(self, user_id: str):
        user = self.repository.get_user_by_id(user_id)
        if not user:
            raise ValueError("Usuario no encontrado")
        return user

    def create_user(self, user_id: str, name: str):
        if self.repository.get_user_by_id(user_id):
            raise ValueError("El usuario ya existe")
        return self.repository.create_user(user_id, name)

    def update_user(self, user_id: str, name: str):
        user = self.repository.update_user(user_id, name)
        if not user:
            raise ValueError("Usuario no encontrado")
        return user

    def delete_user(self, user_id: str):
        user = self.repository.get_user_by_id(user_id)
        if not user:
            raise ValueError("Usuario no encontrado")
        self.repository.delete_user(user_id)
