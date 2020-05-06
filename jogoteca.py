from flask import Flask, render_template, request, redirect, session, flash, url_for,send_from_directory
from flask_mysqldb import MySQL


app = Flask(__name__)
#Definindo chave para conseguir armazenar sessao
app.config.from_pyfile('config.py')

db = MySQL(app)

from views import *




if __name__ == '__main__':
    app.run(debug=True)
# app.run(host='0.0.0.0', port=8080) alternativa para configurar a porta e o host do metodo run