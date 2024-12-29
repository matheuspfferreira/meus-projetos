from typing import Dict, List
from fastapi import APIRouter, HTTPException
from app.classes.criptografia import Criptografia
from app.modelos.modelos_senha import Senha

senhas: List[Senha] = []  # Senhas criadas

router = APIRouter(prefix="/senhas")  # Criando o roteador


# Rota para criar uma senha
@router.post("/criar", response_model=Senha)
def criar_senha(senha: Senha) -> Senha:
    """
    Cria uma nova senha e adiciona à lista de senhas.

    Parâmetros:
        senha (Senha): Objeto contendo a descrição e a chave da senha a ser criada.

    Retorno:
        Senha: O objeto da nova senha criada, com a chave criptografada.
    """
    if any(senha.descricao == s.descricao for s in senhas):
        raise HTTPException(
            status_code=400, detail="Descrição já existente"
            )
            
    nova_senha = Senha(
        descricao=senha.descricao, chave=Criptografia.criptografar_chave(senha.chave)
    )
    senhas.append(nova_senha)
    return nova_senha


# Rota para listar as senhas criadas
@router.get("/listar", response_model=Dict[str, str])
def listar_senhas() -> Dict:
    """
    Lista todas as senhas criadas com suas chaves descriptografadas.

    Retorno:
        Dict: Um dicionário onde as chaves são as descrições das senhas e os valores
              são as respectivas chaves descriptografadas.
    """
    if not senhas:
        raise HTTPException(
            status_code=404, detail="Nenhuma senha criada até o momento"
        )

    senhas_criadas = {
        senha.descricao: Criptografia.descriptografar_chave(senha.chave)
        for senha in senhas
    }
    return senhas_criadas
