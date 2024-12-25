class Formatacao:

    @staticmethod
    def formatar_livro(livro):
        """
        Formata o nome do livro bíblico.

        O método ajusta o nome do livro para que cada palavra comece com uma letra maiúscula
        e remove quaisquer espaços extras no início ou no final da string.

        Parâmetros:
        - livro (str): Nome do livro bíblico.

        Retorno:
        - str: Nome do livro formatado, no estilo 'Title Case' e sem espaços desnecessários.
        """
        return livro.title().strip()
    
    @staticmethod
    def formatar_texto(texto):
        """
        Remove espaços em branco ou caracteres específicos das extremidades de uma string.

        Parâmetros:
        - texto (str): A string que será formatada.

        Retorno:
        - str: A string sem espaços em branco ou caracteres extras no início e no final.
        """
        return texto.strip()
    
    @staticmethod
    def formatar_resposta_api(resposta):
        """
        Formata a resposta retornada pela API Bible API.

        Este método extrai o texto do versículo e sua referência da resposta JSON fornecida pela API.

        Parâmetros:
        - resposta (dict): Dicionário retornado pela API contendo os detalhes da passagem bíblica.
        Espera-se que o dicionário contenha as chaves "text" (conteúdo do versículo) 
        e "reference" (referência do versículo, como "João 3:16").

        Retorno:
        - tuple: Uma tupla contendo o texto do versículo (str) e a referência (str).
        """
        return resposta["text"], resposta["reference"]
    
    @staticmethod
    def formatar_resposta_adicionar_favoritos(opcao_favorito):
        return opcao_favorito.upper().strip()