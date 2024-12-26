from classes.auxiliares.formatacao import Formatacao
from classes.auxiliares.validacao import Validacao

class Passagem:

    def __init__(self, livro, capitulo, versiculo, texto=""):
        """
        Inicializa uma nova passagem bíblica.

        Parâmetros:
        - livro (str): Nome do livro bíblico formatado.
        - capitulo (int): Número do capítulo validado.
        - versiculo (int): Número do versículo validado.
        - texto (str): Conteúdo da passagem bíblica formatada cujo padrão é "".
        """
        self._livro = Formatacao.formatar_livro(livro)
        self._capitulo = Validacao.verificar_capitulo_versiculo(capitulo)
        self._versiculo = Validacao.verificar_capitulo_versiculo(versiculo)
        self._texto = texto

    @property
    def livro(self):
        """
        Retorna o nome do livro bíblico associado à passagem.

        Retorno:
        - str: O nome do livro bíblico.
        """
        return self._livro
    
    @property
    def capitulo(self):
        """
        Retorna o número do capítulo associado à passagem.

        Retorno:
        - int: O número do capítulo.
        """
        return self._capitulo

    @property
    def versiculo(self):
        """
        Retorna o número do versículo associado à passagem.

        Retorno:
        - int: O número do versículo.
        """
        return self._versiculo

    @property
    def texto(self):
        """
        Retorna o texto do versículo associado à passagem.

        Retorno:
        - str: O texto do versículo bíblico.
        """
        return self._texto
    
    @texto.setter
    def texto(self, novo_texto):
        """
        Define o texto do versículo associado à passagem, aplicando formatação.

        O método recebe um novo texto, aplica formatações específicas utilizando
        a classe auxiliar 'Formatacao' e atribui o resultado ao atributo privado '_texto'.

        Parâmetros:
        - novo_texto (str): O novo conteúdo do texto do versículo.
        """
        self._texto = Formatacao.formatar_texto(novo_texto)
