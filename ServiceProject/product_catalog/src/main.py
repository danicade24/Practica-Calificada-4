from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

# Base de datos en memoria
products = {}

@app.get("/products")
def get_products():
    return products

@app.get("/products/{product_id}")
def get_product(product_id: str):
    product = products.get(product_id)
    if product:
        return product
    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/products")
def create_product(product_id: str, name: str, user_id: str):
    if product_id in products:
        raise HTTPException(status_code=400, detail="Product already exists")
    
    # Verificar existencia de usuario en el servicio de gestión de usuarios
    response = requests.get(f"http://user_management:8000/users/{user_id}")
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="User not found")
    
    products[product_id] = {"id": product_id, "name": name, "user_id": user_id}
    return products[product_id]
