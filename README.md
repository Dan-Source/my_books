# My Books Project


##  TECNOLOGIA

Este projeto Django utiliza a biblioteca Django Rest Framework para
servir um Web Service.

## ESCOPO DO PROJETO


  - Este projeto deve permitir que usuários registrem o seu acervo pessoal de livros. 
  - Cada livro possui nome, autor e número de páginas.
  - Um usuário pode acessar e editar apenas os seus livros.
  - Cada livro está relacionado a uma ou nenhuma categoria.
  - É necessário Autenticação para interagir com as API.
  - O projeto deve fornece uma forma de executar o CRUD para os livros e as categorias. 
  - O projecto possui recursos como filtragem de resultados e similares.


Como consumir esta API para enviar mensagens.

## Primeiros Passos

1. Clone do  repositório
2. Entre na pasta do projeto
3. Crie um virtualenv com Python3
  ```
  $ python3 -m venv venv
  ```
4. Ative o virtualenv
   
  ```
  $ . venv/bin/activate
  ```
5. Instale as dependências

  ```
  $ pip install -r requirements.txt
  ```
   
6. Copie o ENV_SAMPLE para um novo arquivo chamado .env que será usado para
armazenar a informações sensivéis da aplicação

7. Execute as migrations
  ```
  $ ./manage.py makemigrations
  $ ./manage.py migrate
  ```
8. Execute a aplicação

  ```
  $ ./manage.py runserver
  ```

# Documentação


## Consulte os seguintes urls:

### APIroot
  - Abra a sua url_base/ (ex.: http://127.0.0.1:8000/register/)
  - Ná pagina 'APIRoot', poderá ser visualizado os endpoints da API.

### Utilizando Swagger:
   - Abra a sua url_base/swagger/ (ex.: http://127.0.0.1:8000/swagger/)


### Utilizando o Redoc:
  - Abra a sua url_base/redoc/ (ex.: http://127.0.0.1:8000/redoc/)

### Ou importe o arquivo do Insominia:
  - Insomnia_MY_BOOK_JSON

## Fique atento a autenticação:

O servidor gera um token que certifica a identidade do usuário.
Assim o cliente pode enviar o token de volta para o servidor como meio que 
verificar a requisição.
