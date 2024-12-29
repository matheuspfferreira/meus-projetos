from pydantic import BaseModel


class Senha(BaseModel):
    descricao: str  # Finalidade da senha
    chave: str  # Chave de acesso
