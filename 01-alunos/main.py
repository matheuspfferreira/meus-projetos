from classes.menu_inicial import Menu_Inicial
from classes.aluno import Aluno
from flask import Flask

def main():

    while True:
    
        # Exibindo o menu
        Menu_Inicial.exibir_menu()

        # Direcionando o usuário
        opcao = Menu_Inicial.recolher_opcao()
        if opcao is None:
            print('Opção inválida.\n')
            Menu_Inicial.limpar_tela()
            continue

        # Executando as funcionalidades
        match opcao:
            case 1:
                Menu_Inicial.limpar_tela()
                nome, turma, mensalidade = Menu_Inicial.recolher_dados()
                Aluno(nome, turma, mensalidade)

            case 2:

                # Criando o núcleo
                app = Flask(__name__)

                # Definindo a rota
                @app.route('/api/alunos/')
                def exibir_alunos():
                    return Aluno.transformar_dados()
                
                # Rodando a aplicação
                app.run()

            case _:
                Menu_Inicial.limpar_tela()
                break

        # Limpando a tela para voltar ao menu
        Menu_Inicial.limpar_tela()

if __name__ == '__main__':
    main()