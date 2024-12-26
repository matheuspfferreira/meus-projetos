from requests import get

class Consulta:

    @staticmethod
    def procurar_passagem(livro, capitulo, versiculo):
        """
        Consulta uma passagem bíblica na API Bible API.

        Este método constrói uma URL com base nos parâmetros fornecidos e realiza
        uma requisição HTTP para obter os dados da passagem bíblica especificada.
        A tradução utilizada é 'Almeida'.

        Parâmetros:
        - livro (str): Nome do livro bíblico (exemplo: "joao").
        - capitulo (int): Número do capítulo da passagem.
        - versiculo (int): Número do versículo da passagem.

        Retorno:
        - dict: Resposta da API em formato JSON contendo os detalhes da passagem bíblica.

        Exceções:
        - requests.exceptions.HTTPError: Lançada se a requisição HTTP falhar (status de erro).
        """ 
        url = f"https://bible-api.com/{livro}+{capitulo}:{versiculo}?translation=almeida"
        response = get(url)
        response.raise_for_status()
        return response.json()       