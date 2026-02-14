import uvicorn
from fastapi import FastAPI
from src.infrastructure.api.router import router

app = FastAPI(title="Microservicio de Usuarios", version="1.0.0")

app.include_router(router, prefix="/api/v1")

@app.get("/")
def home():
    return {"message": "Microservicio de Usuarios con Arquitectura Hexagonal Activo"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)