from flask import Flask, render_template, request, redirect, session, flash, url_for
from dao import JogoDao
from dao import UsuarioDao
from flask_mysqldb import MySQL
from models import Jogo, Usuario
app = Flask(__name__)
#Definindo chave para conseguir armazenar sessao
app.secret_key = 'alura'
app.config['MYSQL_HOST'] = "127.0.0.1"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "root"
app.config['MYSQL_DB'] = "jogoteca"
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)
jogo_dao  = JogoDao(db)
usuario_dao = UsuarioDao(db)



#user1 =Usuario('abilionb', 'Abilio Nogueira', '1234')
#user2 =Usuario('rmelo', 'Renata Melo', '5678')
#user3 =Usuario('Tuser', 'Usuario Teste', 'abcd')

#users = {user1.id: user1,
         #user2.id: user2,
         #user3.id: user3}

#jogo1 = Jogo('Super Mario', 'Acao', 'SNES')
#jogo2 = Jogo('Pokemon Gold', 'RPG', 'GBA')
#lista = [jogo1, jogo2]


@app.route('/')
def index():
    lista = jogo_dao.listar()
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
    #lista.append(jogo)
    jogo_dao.salvar(jogo)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    #Realizando um query para buscar a proxima pagina pos login
    proxima = request.args.get('proxima')
    return render_template('login.html',proxima = proxima)


@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = usuario_dao.buscar_por_id(request.form['usuario'])
    if usuario:
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
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