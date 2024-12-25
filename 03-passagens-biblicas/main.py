from classes.auxiliares.menu import Menu
from classes.auxiliares.formatacao import Formatacao
from classes.principais.lista_favoritos import Lista_Favoritos
from classes.principais.passagem import Passagem
from classes.principais.consulta import Consulta

def main():

    # Criando a lista de favoritos
    favoritos = Lista_Favoritos()

    while True:

        # Exibindo o menu de opções
        Menu.exibir_menu_inicial()

        # Recebendo a opção desejada
        opcao = Menu.receber_opcao()

        # Direcionando o usuário
        match (opcao):
            case 1:

                # Recebendo os dados da passagem
                Menu.limpar_tela()
                livro, capitulo, versiculo = Menu.receber_dados_passagem()

                # Criando uma passagem
                passagem = Passagem(livro, capitulo, versiculo)

                # Efetuando a consulta
                resposta = Consulta.procurar_passagem(passagem.livro, passagem.capitulo, passagem.versiculo)
                texto, referencia = Formatacao.formatar_resposta_api(resposta)

                # Incluindo o texto no atributo da instância
                passagem.texto = texto

                # Exibindo a passagem
                Menu.limpar_tela()
                print(f"\n{passagem.texto} - {referencia}\n")

                # Adicionando a passagem à lista de favoritos
                deseja_adicionar = Menu.receber_resposta_adicionar_favoritos()
                if deseja_adicionar:
                    favoritos.adicionar_passagem(referencia, passagem.texto)


            case 2:
                pass

            case _:
                break

        # Limpando a tela para retornar
        Menu.limpar_tela()
                
    

if __name__ == '__main__':
    main()