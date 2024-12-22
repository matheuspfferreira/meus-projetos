class Aluno:

    # Atributo de classe
    alunos = []

    # Métodos especiais
    def __init__(self, nome, turma, mensalidade):
        """
        Inicializa um novo objeto Aluno com nome, turma e mensalidade.
        Adiciona o aluno à lista de alunos da classe.
        """
        self._nome = self._formatar(nome)
        self._turma = self._formatar(turma)
        self._mensalidade = self._verificar_mensalidade(mensalidade)
        Aluno.alunos.append(self)

    def __str__(self):
        """
        Retorna uma representação textual do objeto Aluno.
        Mostra o nome, turma e mensalidade formatados como string.
        """
        return f'Nome: {self._nome} - {self.
        _turma} - Mensalidade: R$ {self._mensalidade}'

    # Métodos de formatação
    @staticmethod
    def _formatar(valor):
        """
        Formata o valor como título, capitalizando as palavras.
        """
        return valor.title()
    
    @staticmethod
    def _verificar_mensalidade(valor):
        """
        Verifica se o valor é um float válido e não negativo.
        Retorna o valor se válido, ou 0.0 caso contrário.
        """
        if isinstance(valor, float) and valor >= 0.0:
            return valor
        return 0.0
    
    # Método de classe
    @classmethod
    def transformar_dados(cls):
        """
        Transforma os dados dos alunos em um dicionário estruturado.
        Retorna um dicionário com o nome do aluno como chave e a turma e mensalidade como valores.
        """
        dados = {}
        for aluno in cls.alunos:
            dados[aluno._nome] = {"turma: ": aluno._turma, 
                                        "mensalidade: ": aluno._mensalidade}
        return dados