from fastapi import FastAPI
from fastapi.responses import JSONResponse
from uvicorn import Config, Server, run
from threading import Thread

class Servidor:

    def __init__(self, lista_favoritos):
        """
        Inicializa a classe configurando o FastAPI e a lista de passagens favoritas.

        Parâmetros:
            lista_favoritos (object): Objeto contendo as passagens favoritas do usuário.

        Atributos:
            _app (FastAPI): Instância do FastAPI para gerenciar o servidor.
            _lista_favoritos (list): Lista contendo as passagens favoritas do usuário.
        """
        self._app = FastAPI()
        self._lista_favoritos = lista_favoritos.passagens_favoritas
        self._configurar_rotas()

    def _configurar_rotas(self):
        """
        Configura as rotas para a aplicação FastAPI.

        Rota configurada:
            - GET /lista-favoritos/: Retorna a lista de passagens favoritas ou uma mensagem
            de erro caso a lista esteja vazia.

        Retorno:
            - JSONResponse: Um JSON com uma mensagem de erro.
        """
        @self._app.get("/lista-favoritos/")
        def exibir_lista_favoritos():
            if not self._lista_favoritos:
                return JSONResponse(content={"Erro": "A lista de favoritos está vazia"})
            return self._lista_favoritos
        
    def iniciar_segundo_plano(self):
        """
        Inicia o servidor FastAPI.

        Configura o servidor para rodar localmente no endereço 127.0.0.1 e na porta 8000.
        """
        config = Config(self._app, host="127.0.0.1", port=8000)
        server = Server(config)
        thread = Thread(target=server.run, daemon=True)
        thread.start()
        