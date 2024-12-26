class Lista_Favoritos:

    def __init__(self):
        """
        Inicializa uma instância da classe.

        Atributos:
        - self._passagens (dict): Dicionário que armazena todas as passagens adicionadas.
        """
        self._passagens_favoritas = {}

    @property
    def passagens_favoritas(self):
        """
        Retorna as passagens favoritas armazenadas.

        Este método é uma propriedade (getter) que permite acessar o dicionário de passagens favoritas da instância.

        Retorno:
        - dict: O dicionário de passagens favoritas.
        """
        return self._passagens_favoritas

    def adicionar_passagem(self, referencia, texto):
        """
        Adiciona uma nova passagem ao dicionário de passagens.

        Parâmetros:
        - passagem (str): A passagem que será adicionada ao dicionário de passagens.
        """
        self._passagens_favoritas[referencia] = texto