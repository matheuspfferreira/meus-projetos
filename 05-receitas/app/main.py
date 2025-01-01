from fastapi import FastAPI
from uvicorn import run
from app.routers.routers_receita import router


app = FastAPI()  # Criando a aplicação
app.include_router(router)  # Importando as rotas


if __name__ == "__main__":
    run(app=app, host="127.0.0.1", port=8001)
