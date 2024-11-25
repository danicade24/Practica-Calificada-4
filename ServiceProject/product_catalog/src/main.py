from fastapi import FastAPI, HTTPException

app = FastAPI()

# Almacenamos los usuarios en un diccionario
users = {}

"""Implementamos los métodos CRUD para user_management"""

# Listar todos los usuarios
@app.get("/users")
def get_users():
    return {"users": users}  # Devuelve un diccionario con la clave de usuarios

# Obtener usuario por ID
@app.get("/users/{user_id}")
def get_user(user_id: str):
    user = users.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"user": user}  # Devuelve un diccionario con la clave "user"

# Crear usuario
@app.post("/users")
def create_user(user_id: str, name: str):
    if user_id in users:  # Verifica si el usuario ya existe
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    users[user_id] = {"id": user_id, "name": name}
    return {"user": users[user_id]}

# Actualizar usuario
@app.put("/users/{user_id}")
def update_user(user_id: str, name: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    users[user_id]["name"] = name
    return {"user": users[user_id]}

# Eliminar usuario por ID
@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    del users[user_id]
    return {"message": "Usuario eliminado"}
