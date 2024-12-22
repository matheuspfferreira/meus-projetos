from os import system

class Menu_Inicial:
    
    # Métodos de saída
    @staticmethod
    def exibir_menu():
        """
        Exibe o menu de gerenciamento de alunos.
        """
        print("""\n*****Gerenciamento de Alunos****\n
        1. Cadastrar aluno.
        2. Exibir alunos cadastrados.
        3. Sair\n""")

    @staticmethod
    def limpar_tela():
        system('cls')
        
    # Métodos de entrada
    @staticmethod
    def recolher_opcao():
        """
        Solicita e valida a opção escolhida pelo usuário.
        Retorna a opção se válida, ou None caso contrário.
        """
        opcao = int(input("Informe a opção desejada: "))
        if opcao in range(1, 4):
            return opcao
        return None

    @staticmethod
    def recolher_dados():
        """
        Coleta os dados de um aluno via entrada do usuário.
        Retorna o nome, turma e mensalidade informados.
        """
        nome = input("\nInforme o nome do aluno: ")
        turma = input("Informe a turma do aluno: ")
        mensalidade = float(input("Informe a mensalidade do aluno: "))
        return nome, turma, mensalidade