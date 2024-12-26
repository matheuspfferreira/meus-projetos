# Gerenciador de Passagens Bíblicas

Este projeto é uma aplicação para gerenciar passagens bíblicas, permitindo que o usuário busque por passagens específicas e as adicione a uma lista de favoritos. A aplicação utiliza a API pública [Bible API](https://bible-api.com/) para consultar as passagens e expõe uma API local desenvolvida com FastAPI.

## Funcionalidades

- **Busca de passagens bíblicas**: Permite que o usuário procure qualquer passagem utilizando a API Bible API.
- **Gerenciamento de favoritos**: Possibilita adicionar passagens bíblicas a uma lista de favoritos.
- **Servidor local com API**: Exibe a lista de passagens favoritas através de um servidor Uvicorn rodando com FastAPI.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **FastAPI**: Framework para criação de APIs rápidas e eficientes.
- **Uvicorn**: Servidor ASGI para executar a aplicação FastAPI.
- **Requests**: Biblioteca para realizar requisições HTTP.