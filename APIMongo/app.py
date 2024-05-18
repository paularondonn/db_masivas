from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="REST API with MongoDB",
    description="Esta api es para realizar pruebas de conexion a mongodb",
    version="0.0.1"
)

app.include_router(user)
