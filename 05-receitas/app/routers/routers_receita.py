from typing import Dict
from fastapi import APIRouter, HTTPException
from app.models.models_receita import Receita, CriarReceita, PesquisarReceita


router = APIRouter(prefix="/receitas")  # Roteador para as rotas
receitas: Dict[int, Receita] = {}  # Receitas já criadas
contador_id: int = 1  # Número do identificador


@router.post("/criar", response_model=Receita)
def criar_receita(receita: CriarReceita) -> Receita:
    if any(receita_cadastrada["nome"] == receita.nome for receita_cadastrada in receitas.values()):
        raise HTTPException(
            status_code=400, 
            detail=f"A receita de {receita.nome} já está cadastrada"
        )

    global contador_id
    nova_receita = Receita(id=contador_id, **receita.model_dump())
    receitas[nova_receita.id] = {
        "nome": nova_receita.nome,
        "ingredientes": nova_receita.ingredientes,
    }
    contador_id += 1
    return nova_receita


@router.get("/pesquisar", response_model=Dict[str, str])
def pesquisar_receita(pesquisa: PesquisarReceita) -> Dict[str, str]:
    ingredientes_encontrados = [
        ingrediente
        for ingrediente in pesquisa.ingredientes_disponiveis
        if ingrediente in receitas.items["ingredientes"]
    ]

    return ingredientes_encontrados
