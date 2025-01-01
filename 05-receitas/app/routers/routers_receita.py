from typing import Dict, List
from fastapi import APIRouter, HTTPException, Query
from app.models.models_receita import CriarReceita, Receita


router = APIRouter(prefix="/receitas")  # Roteador para as rotas
receitas: Dict[int, Receita] = {}  # Receitas já criadas
contador_id: int = 1  # Número do identificador


@router.post("/criar", response_model=Receita)
def criar_receita(receita: CriarReceita) -> Receita:
    """
    Cadastra uma nova receita no sistema.

    Parâmetros:
        receita (CriarReceita): Objeto contendo o nome e os ingredientes da nova receita.

    Retorno:
        Receita: Objeto contendo os detalhes da receita cadastrada, incluindo o ID.

    Exceções:
        HTTPException: Lançada caso uma receita com o mesmo nome já esteja cadastrada.
    """
    if any(
        receita_cadastrada["nome"] == receita.nome
        for receita_cadastrada in receitas.values()
    ):
        raise HTTPException(
            status_code=400, detail=f"A receita de {receita.nome} já está cadastrada"
        )

    global contador_id
    nova_receita = Receita(id=contador_id, **receita.model_dump())
    receitas[nova_receita.id] = {
        "nome": nova_receita.nome,
        "ingredientes": nova_receita.ingredientes,
    }
    contador_id += 1
    return nova_receita


@router.get("/pesquisar/")
def pesquisar_receita(
    ingredientes_disponiveis: List[str] = Query(...),
) -> Dict[str, List[str]]:
    """
    Pesquisa receitas com base nos ingredientes disponíveis.

    Parâmetros:
        ingredientes_disponiveis (List[str]): Lista de ingredientes disponíveis fornecida pelo usuário.

    Retorno:
        Dict[str, List[str]]: Um dicionário contendo os nomes das receitas possíveis como chave
                              e seus ingredientes como valores.

    Exceções:
        HTTPException: Lançada caso nenhuma receita seja encontrada com os ingredientes fornecidos.
    """
    receitas_possiveis = {
        receita["nome"]: receita["ingredientes"]
        for receita in receitas.values()
        if any(
            ingrediente in ingredientes_disponiveis
            for ingrediente in receita["ingredientes"]
        )
    }

    if not receitas_possiveis:
        raise HTTPException(
            status_code=404,
            detail="Nenhuma receita foi encontrada com esses ingredientes",
        )
    return receitas_possiveis
