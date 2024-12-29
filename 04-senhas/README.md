# API de Gerenciamento de Senhas

Esta API foi desenvolvida para gerenciar senhas de forma segura, permitindo criar e listar senhas com funcionalidades de criptografia para proteção das chaves.

## Funcionalidades

- **Criar Senha**: Permite informar uma descrição e uma chave. A chave é criptografada antes de ser armazenada.
- **Listar Senhas**: Retorna todas as senhas criadas com as chaves descriptografadas, garantindo a segurança e a usabilidade dos dados.

## Tecnologias Utilizadas

- **Python**: Linguagem principal para desenvolvimento.
- **FastAPI**: Framework utilizado para a construção da API.
- **Uvicorn**: Servidor ASGI para executar a aplicação.