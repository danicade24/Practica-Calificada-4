# PC4: ServiceProject

## Descripción
Este proyecto contiene dos servicios independientes conectados:
1. **Gestión de Usuarios**: Un servicio que sirve manejar usuarios.
2. **Catálogo de Productos**: Un servicio que sirve para gestionar productos y asociarlo con lso usuarios.

## Requisitos
- Docker
- Docker Compose

### Clonar el repositorio:
    ```bash
    git clone https://github.com/danicade24/Practica-Calificada-4.git

    cd ServiceProject
    ``` 

## Proyecto 1: Gestión de Usuarios

### 1. Funcionalidad

Implementamos el codigo necesario para que pueda crear, leer, eliminar y actualizar 

### Código para operaciones CRUD
```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Almacenamos los usuarios en un diccionario
users = {}

"""Implementamos los métodos CRUD para user_management"""

# Listar todos los usuarios
@app.get("/users")
def get_users():
    return {"users": users}  # Devuelve un diccionario con la clave "users"

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
```

**Endpoints:**
   - **GET `/users`:** Debería devolver un diccionario vacio al inicio.
   - **POST `/users`:** Crea un usuario con `user_id` y `name`.
   - **GET `/users/{user_id}`:** Obtiene la información de un usuario creado.
   - **PUT `/users/{user_id}`:** Actualiza el nombre de un usuario existente.
   - **DELETE `/users/{user_id}`:** Elimina un usuario.



### 2. Diseño

### 3. Pruebas

### 4. Métricas




## Proyecto 2: Catálogo de Productos

### 1. Funcionalidad

### 2. Diseño

### 3. Pruebas

### 4. Métricas
