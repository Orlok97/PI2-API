# São Vicente Conecta - Portal da Zeladoria

## Descrição

Este projeto integrador foi desenvolvido como parte do curso de Engenharia de Computação, Ciência de Dados e Tecnologia da Informação pela faculdade UNIVESP.

### Sobre o Projeto

A API desenvolvida tem como objetivo facilitar a comunicação do munícipe vicentino com a prefeitura de São Vicente através de um portal que conecta ambas as partes, promovendo maior eficácia na gestão e resolução de solicitações de zeladoria urbana.

## Endpoints
### URL Base
```sh
https://orlok.pythonanywhere.com/
```
### Citizen
#### POST
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
#### GET
Endpoint para listar munícipes ou buscar um determinado munícipe pelo id, se não for passado o id a resposta será uma lista com todos os munícipes cadastrados.

```sh
api/v1/citizen/<int:id>
```
**JSON Headers**

```json
"Authorization" : "Bearer <token_de_acesso>",
"Content-Type" : "application/json"
```
#### PUT
Endpoint para alterar os dados de um determinado munícipe pelo id

```sh
api/v1/citizen/<int:id>
```

**JSON Headers**
```json
"Authorization" : "Bearer <token_de_acesso>",
"Content-Type" : "application/json"
```
***JSON Body***
```json
"nome": "seu nome",
"telefone": "seu telefone",
"senha": "sua senha"
```

#### DELETE
Endpoint para deletar um determinado munícipe pelo id.
```sh
api/v1/citizen/<int:id>
```
***JSON Headers***
```json
"Authorization" : "Bearer <token_de_acesso",
"Content-Type": "application/json"
```






