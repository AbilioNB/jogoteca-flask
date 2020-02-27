from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
#Definindo chave para conseguir armazenar sessao
app.secret_key = 'alura'

class Jogo:
    def __init__(self,nome,categoria,console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

class Usuario:
    def __init__(self,id,nome,senha):
        self.id = id
        self.nome = nome
        self.senha = senha



user1 =Usuario('abilionb', 'Abilio Nogueira', '1234')
user2 =Usuario('rmelo', 'Renata Melo', '5678')
user3 =Usuario('Tuser', 'Usuario Teste', 'abcd')

users = {user1.id: user1,
         user2.id: user2,
         user3.id: user3}

jogo1 = Jogo('Super Mario', 'Acao', 'SNES')
jogo2 = Jogo('Pokemon Gold', 'RPG', 'GBA')
lista = [jogo1, jogo2]


@app.route('/')
def index():
    return render_template('lista.html', titulo ='Jogos', jogos = lista)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session ['usuario_logado'] == None:
        return  redirect(url_for('login', proxima = url_for('novo')))
    return render_template('novo.html', titulo='Adicionar Game')


@app.route('/criar', methods=['POST',])
def adicionar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    #Realizando um query para buscar a proxima pagina pos login
    proxima = request.args.get('proxima')
    return render_template('login.html',proxima = proxima)


@app.route('/autenticar', methods=['POST',])
def autenticar():

    if request.form['usuario'] in users:
        usuario = request.form['usuario']
        if users[usuario].senha == request.form['senha']:
            session['usuario_logado'] = usuario
            flash(usuario.nome + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Não logado, tente de novo!')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect(url_for('index'))


app.run(debug=True)
# app.run(host='0.0.0.0', port=8080) alternativa para configurar a porta e o host do metodo run