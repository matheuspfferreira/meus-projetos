class Criptografia:

    @staticmethod
    def criptografar_chave(chave: str) -> str:
        if isinstance(chave, str):
            return chave[::-1]
        raise ValueError("O parâmetro 'chave' deve ser uma string")

    @staticmethod
    def descriptografar_chave(chave_criptografada: str) -> str:
        if isinstance(chave_criptografada, str):
            return chave_criptografada[::-1]
        raise ValueError("O parâmetro 'chave' deve ser uma string")
