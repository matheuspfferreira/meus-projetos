class Validacao:

    @staticmethod
    def verificar_capitulo_versiculo(valor):
        """
        Verifica se o valor fornecido é um número inteiro.

        Parâmetros:
        - valor (qualquer tipo): Valor a ser validado.

        Retorno:
        - valor (int): Retorna o valor se ele for um inteiro válido.

        Exceções:
        - ValueError: Lançada se o valor não for um número inteiro.
        """
        if isinstance(valor, int):
            return valor
        raise ValueError("Informe apenas números inteiros.\n")
            
    @staticmethod
    def verificar_opcao(opcao, quantidade_opcoes):
        """
        Verifica se a opção fornecida está dentro do intervalo de opções válidas.

        Parâmetros:
        - opcao (int): A opção selecionada pelo usuário.
        - quantidade_opcoes (int): O número total de opções disponíveis no menu.

        Retorno:
        - bool: Retorna True se a opção for válida (dentro do intervalo de 1 até quantidade_opcoes, inclusive).
                Caso contrário, retorna False.
        """
        if opcao in range(1, quantidade_opcoes+1):
            return True
        return False
    
    