# Desvendando em Flask

Esse projeto abranje meu aprendizado como desenvolvedor python, mais apropriadamente o Flask.

### Sobre o flask

O Flask é um microframeork baseado em python onde podemos construir nossas Api's web com uma curva de aprendizado bem reduziada. 

E por ser python, é bastante elegante.

Aqui temos um link pra documentação do [flask](https://palletsprojects.com/p/flask/)

## Objetivo: 

A primeira parte temos a prática sobre o curso de Introdução ao Flask da Alura onde o projeto consistia num crud (sem a opção de remoção).

Nome do projeto: **Jogoteca** 
Descrição: Um pequeno site de listagem de jogos de diferentes plataformas
Rotas e Funções:
* / : Rota principal onde temos a listagens dos jogos 
* novo: Adiciona um novo jogo a listagem 
* login : Faz verificação de credenciais 
* logout: Realiza o Logoff dos usuario anteriormente logado


Observações: 
* Não foram usados praticas de OO como encapsulamento de objetos pois o foco se tornou desenvolver a aplicação em sí, entretanto não se descarta a importância do OO no flask.

## Para Devs

### Blibliotecas utilizadas:
* Flask: Os parametros utilziados do flash estão na primeira linha do arquivo jogoteca.py

* Bootstrap 4: Foi descarregado direto do próprio [site](https://getbootstrap.com/)<br>
``Foi adicioniado apenas o arquivo bootstrap.css``

### Para utilizar
1. Clonar o projeto
2. Instalar o Flask
````
 pip3 install flask==0.12.2
````
3. Executar a aplicação pelo arquivo ``jogoteca.py``

## Desenvolvimento futuro

O objetivo é no segundo modulo adicionar uma camada de persistencia com banco de dados Mysql.

