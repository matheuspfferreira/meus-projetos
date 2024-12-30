from typing import List
from pydantic import BaseModel


class CriarReceita(BaseModel):
    nome: str  
    ingredientes: List[str]  


class Receita(CriarReceita):
    id: int  


class PesquisarReceita(BaseModel):
    ingredientes_disponiveis: List[str]  
