from typing import List
from pydantic import BaseModel


class CriarReceita(BaseModel):
    """
    Modelo de dados para criar uma receita.

    Atributos:
        nome (str): Nome da receita.
        ingredientes (List[str]): Lista de ingredientes necessários para a receita.
    """

    nome: str
    ingredientes: List[str]


class Receita(CriarReceita):
    """
    Modelo de dados para representar uma receita com ID.

    Herda:
        CriarReceita: Inclui os atributos 'nome' e 'ingredientes'.

    Atributos:
        id (int): Identificador único da receita.
    """

    id: int
