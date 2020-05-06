from flask import  render_template, request, redirect, session, flash, url_for,send_from_directory
from dao import JogoDao
from dao import UsuarioDao
import time
from jogoteca import db,app
from helpers import deleta_arquivo, recupera_imagem

jogo_dao  = JogoDao(db)
usuario_dao = UsuarioDao(db)


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
    jogo = jogo_dao.salvar(jogo)
    #Para buscar um arquivo
    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    arquivo.save(f'{upload_path}/capa{jogo.id}-{timestamp}.jpg')
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

@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session ['usuario_logado'] == None:
        return  redirect(url_for('login', proxima = url_for('editar')))
    jogo = jogo_dao.busca_por_id(id)

    nome_imagem = recupera_imagem(id)
    flash(nome_imagem)
   #Retirar aq
    #deleta_arquivo(id)

    return render_template('editar.html', titulo='Editando Jogo', jogo= jogo, capa_jogo= nome_imagem)




@app.route('/atualizar', methods=['POST', ])
def atualizar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console, id = request.form['id'])

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    deleta_arquivo(jogo.id)
    arquivo.save(f'{upload_path}/capa{jogo.id}-{timestamp}.jpg')
    jogo_dao.salvar(jogo)
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect(url_for('index'))

@app.route('/deletar/<int:id>')
def deletar(id):
    jogo_dao.deletar(id)
    deleta_arquivo(id)
    flash("Jogo removido")
    return redirect(url_for('index'))
@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads',nome_arquivo)