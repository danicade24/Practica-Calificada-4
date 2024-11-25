class UserRepository:
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
