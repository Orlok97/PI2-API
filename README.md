# São Vicente Conecta - Portal da Zeladoria

## Descrição

Este projeto integrador foi desenvolvido como parte do curso de Engenharia de Computação, Ciência de Dados e Tecnologia da Informação pela faculdade UNIVESP.

### Sobre o Projeto

A API desenvolvida tem como objetivo facilitar a comunicação do munícipe vicentino com a prefeitura de São Vicente através de um portal que conecta ambas as partes, promovendo maior eficácia na gestão e resolução de solicitações de zeladoria urbana.

## Tabela de Conteúdo

1. [URL Base](#url-base)
2. [Endpoints de Citizen](#citizen)
   - [POST - Cadastrar um novo munícipe](#post)
   - [GET - Listar munícipes ou buscar por ID](#get)
   - [PUT - Atualizar dados de um munícipe](#put)
   - [DELETE - Remover um munícipe](#delete)
3. [Endpoints de Admin](#admin)
   - [POST - Cadastrar um novo administrador](#post-admin)
   - [GET - Listar administradores ou buscar por ID](#get-admin)
   - [PUT - Atualizar dados de um administrador](#put-admin)
   - [DELETE - Remover um administrador](#delete-admin)
4. [Endpoints de Auth](#auth)
   - [POST - Login](#post-auth)
5. [Endpoints de Service](#service)
   - [POST - Cadastrar um novo serviço](#post-service)
   - [GET - Listar serviços ou buscar por ID](#get-service)
   - [PUT - Atualizar dados de um serviço](#put-service)
   - [DELETE - Remover um serviço](#delete-service)
6. [Endpoints de Janitorial](#janitorial)
   - [POST - Cadastrar uma nova solicitação de zeladoria](#post-janitorial)
   - [GET - Listar solicitações de zeladoria ou buscar por ID](#get-janitorial)
   - [PUT - Atualizar dados de uma solicitação de zeladoria](#put-janitorial)
   - [DELETE - Remover uma solicitação de zeladoria](#delete-janitorial)
7. [Endpoints de Employee](#employee)
   - [POST - Cadastrar um novo funcionário](#post-employee)
   - [GET - Listar funcionários ou buscar por ID](#get-employee)
   - [PUT - Atualizar dados de um funcionário](#put-employee)
   - [DELETE - Remover um funcionário](#delete-employee)

## URL Base
```sh
https://orlok.pythonanywhere.com/
```

## Citizen

### POST

Endpoint para cadastrar um novo munícipe.
```sh
api/v1/citizen
```
**Requisição JSON**:

```json
{
  "nome": "seu nome",
  "email": "seu email",
  "telefone": "seu telefone",
  "senha": "sua senha"
}
```

### GET

Endpoint para listar munícipes ou buscar um determinado munícipe pelo id. Se não for passado o id, a resposta será uma lista com todos os munícipes cadastrados.

```sh
api/v1/citizen/<int:id>
```
**JSON Headers**

```json
"Authorization": "Bearer <token_de_acesso>",
"Content-Type": "application/json"
```

### PUT

Endpoint para alterar os dados de um determinado munícipe pelo id.

```sh
api/v1/citizen/<int:id>
```
**JSON Headers**
```json
"Authorization": "Bearer <token_de_acesso>",
"Content-Type": "application/json"
```
**JSON Body**
```json
{
  "nome": "seu nome",
  "telefone": "seu telefone",
  "senha": "sua senha"
}
```

### DELETE

Endpoint para deletar um determinado munícipe pelo id.
```sh
api/v1/citizen/<int:id>
```
**JSON Headers**
```json
"Authorization": "Bearer <token_de_acesso>",
"Content-Type": "application/json"
```

## Admin

### POST

Endpoint para cadastrar um novo administrador.
```sh
api/v1/admin
```
***JSON Body***
```json
"nome":"nome do admin",
"email": "email do admin",
"senha": "senha do admin"
```
O admin também pode ser cadastrado ao rodar o script admin_setup.py dentro do diretório do projeto, como mostrado no exemplo abaixo:
```sh
python admin_setup.py
```

### GET

Endpoint para listar administradores ou buscar um administrador pelo id.
```sh
api/v1/admin/<int:id>
```

### PUT

Endpoint para atualizar dados de um administrador pelo id.
```sh
api/v1/admin/<int:id>
```

### DELETE

Endpoint para deletar um administrador pelo id.
```sh
api/v1/admin/<int:id>
```

## Auth

### POST

Endpoint para login.
```sh
api/v1/auth
```
Na chave permission, o valor deve receber "citizen" "admin", ou "employee".

***JSON Body***
```json
"email": "email do úsuario",
"senha": "senha do úsuario",
"permission": "permissão do úsuario"
```
***JSON Response***
```json
"response": "úsuario autenticado",
"token": "token retornado",
"status": "ok",
"permission": "permissão retornada"

```
### GET
Endpoint para buscar dados do úsuario autenticado.
permissões:"citizen", "admin", "employee"
```sh
api/v1/auth/<str:permission>
```
***JSON Headers***
```json
"Authorization": "Bearer <token_de_acesso>",
"Content-Type": "application/json"
```
## Service

### POST

Endpoint para cadastrar um novo serviço.
```sh
api/v1/service
```

### GET

Endpoint para listar serviços ou buscar um serviço pelo id.
```sh
api/v1/service/<int:id>
```

### PUT

Endpoint para atualizar dados de um serviço pelo id.
```sh
api/v1/service/<int:id>
```

### DELETE

Endpoint para deletar um serviço pelo id.
```sh
api/v1/service/<int:id>
```

## Janitorial

### POST

Endpoint para cadastrar uma nova solicitação de zeladoria.
```sh
api/v1/janitorial
```

### GET

Endpoint para listar solicitações de zeladoria ou buscar uma solicitação pelo id.
```sh
api/v1/janitorial/<int:id>
```

### PUT

Endpoint para atualizar dados de uma solicitação de zeladoria pelo id.
```sh
api/v1/janitorial/<int:id>
```

### DELETE

Endpoint para deletar uma solicitação de zeladoria pelo id.
```sh
api/v1/janitorial/<int:id>
```

## Employee

### POST

Endpoint para cadastrar um novo funcionário.
```sh
api/v1/employee
```

### GET

Endpoint para listar funcionários ou buscar um funcionário pelo id.
```sh
api/v1/employee/<int:id>
```

### PUT

Endpoint para atualizar dados de um funcionário pelo id.
```sh
api/v1/employee/<int:id>
```

### DELETE

Endpoint para deletar um funcionário pelo id.
```sh
api/v1/employee/<int:id>
```

