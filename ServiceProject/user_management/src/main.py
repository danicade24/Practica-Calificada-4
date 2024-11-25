from fastapi import FastAPI
from controllers.user_controller import router

app = FastAPI()

# Registrar las rutas del controlador
app.include_router(router)
