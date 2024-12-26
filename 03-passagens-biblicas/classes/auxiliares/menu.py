from classes.auxiliares.validacao import Validacao
from classes.auxiliares.formatacao import Formatacao
from os import system

class Menu:

    @staticmethod
    def exibir_menu_inicial():
        """
        Exibe o menu inicial do Gerenciador de Passagens Bíblicas no terminal.

        O menu apresenta as opções disponíveis para o usuário, como procurar por uma passagem bíblica ou sair do programa.
        """
        print("""\n*****Gerenciador de Passagens Bíblicas*****\n
              [1] Procurar por passagem bíblica.
              [2] Exibir passagens favoritas.
              [3] Sair.\n""")

    @staticmethod
    def limpar_tela():
        """
        Limpa a tela do console.

        Este método utiliza o comando do sistema operacional para limpar o console:
        - Em sistemas Windows, utiliza o comando 'cls'.
        """
        system('cls')

    @staticmethod   
    def receber_opcao():
        """
        Solicita ao usuário que informe uma opção do menu e valida a entrada.

        Retorno:
        - int: A opção selecionada pelo usuário, se válida.

        Exceções:
        - ValueError: Lançada se a opção informada não for válida.
        """ 
        opcao = int(input("Informe a opção que deseja: \n>>>>> "))
        if Validacao.verificar_opcao(opcao, 3):
            return opcao
        raise ValueError("Opção inválida.\n")

    @staticmethod
    def receber_dados_passagem():
        """
        Solicita ao usuário os dados de uma passagem bíblica: livro, capítulo e versículo(s).

        Retorno:
        - tuple: Uma tupla contendo o livro (str), capítulo (int) e versículo (int) fornecidos pelo usuário.
        """
        livro = input("Informe o livro: \n>>>>> ")
        capitulo = int(input("\nInforme o capítulo: \n>>>>> "))
        versiculo = int(input("\nInforme o versículo: \n>>>>> "))
        return livro, capitulo, versiculo
    
    def receber_resposta_adicionar_favoritos():
        """
        Solicita ao usuário a confirmação para adicionar uma passagem à lista de favoritos.

        A entrada é formatada e validada para aceitar apenas "SIM" (Sim) ou "NÃO" (Não).
        Se a entrada for inválida, uma exceção é levantada.

        Retorno:
        - bool: Retorna True se o usuário optar por adicionar ("SIM"), ou False para não adicionar ("NÃO").

        Exceções:
        - ValueError: Lançada se a entrada do usuário não for "SIM" ou "NÃO".
        """
        opcao_favorito = input("Deseja adicionar essa passagem à lista de favoritos (SIM/NÃO)? \n>>>>> ")
        opcao_formatada = Formatacao.formatar_resposta_adicionar_favoritos(opcao_favorito)
        if opcao_formatada not in ["SIM", "NÃO"]:
            raise ValueError("Opção inválida.\n")
        return opcao_formatada == "SIM"
    
    @staticmethod
    def exibir_aviso_servidor():
        """
        Exibe uma mensagem informando que o servidor está rodando em segundo plano.

        A mensagem inclui o endereço da rota para acessar a lista de passagens bíblicas.
        """
        print("A sua lista de passagens bíblicas está em segundo plano.\nAcesse: http://127.0.0.1:8000/lista-favoritos \n")

    @staticmethod
    def receber_resposta_voltar_menu():
        """
        Solicita ao usuário que pressione Enter para retornar ao menu principal.

        A entrada do usuário é validada:
            - Se o usuário pressionar Enter sem digitar nada, retorna True.
            - Caso contrário, retorna False.

        Retorno:
            - bool: True se o usuário pressionar Enter, False caso contrário.
        """
        deseja_voltar = input("Pressione enter para retormar ao menu: \n>>>>> ")
        return deseja_voltar == ""