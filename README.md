# São Vicente Conecta - Portal da Zeladoria

## Descrição

Este projeto integrador foi desenvolvido como parte do curso de Engenharia de Computação, Ciência de Dados e Tecnologia da Informação pela faculdade UNIVESP.

### Sobre o Projeto

A API desenvolvida tem como objetivo facilitar a comunicação do munícipe vicentino com a prefeitura de São Vicente através de um portal que conecta ambas as partes, promovendo maior eficácia na gestão e resolução de solicitações de zeladoria urbana.

## Endpoints

### citizen
#### POST
Endpoint para cadastrar um novo munícipe.
```sh
https://orlok.pythonanywhere.com/api/v1/citizen
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
Endpoint para listar ou buscar um determinado usuario pelo id, se não for passado o id a resposta será uma lista com todos os úsuarios cadastrados.

```sh
https://orlok.pythonanywhere.com/api/v1/citizen/<int: id>
```
**JSON Headers**

```json
"Authorization" : "Bearer <token_de_acesso>",
"Content-Type" : "application/json"
```


