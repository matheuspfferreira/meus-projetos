from fastapi import FastAPI
from uvicorn import run
from app.roteadores import roteadores_senha

app = FastAPI()  # Criando a aplicação

app.include_router(roteadores_senha.router)  # Importando as rotas

if __name__ == "__main__":
    run(app=app, host="127.0.0.1", port=8000)
