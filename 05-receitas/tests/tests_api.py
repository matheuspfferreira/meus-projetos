from typing import List
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)  # Criando um cliente de teste
nome: str = "bolo-cenoura"  # Nome da receita teste
ingredientes: List[str] = ["cenoura", "ovo", "leite"]  # Ingredientes da receita teste


def test_criar_receita():
    response = client.post(
        "/receitas/criar",
        json={"nome": nome, "ingredientes": ingredientes},
    )
    assert response.status_code == 200
    assert response.json()["nome"] == nome
    assert response.json()["ingredientes"] == ingredientes


def test_pesquisar_receita():
    response = client.get("/receitas/pesquisar", params={"ingredientes_disponiveis": ingredientes})
    assert response.status_code == 200
    assert response.json()[nome] == ingredientes
    