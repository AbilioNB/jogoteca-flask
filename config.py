import os



SECRET_KEY = 'alura'
#Comandos do BD
MYSQL_HOST = "127.0.0.1"
MYSQL_USER = "root"
MYSQL_PASSWORD = "root"
MYSQL_DB = "jogoteca"
MYSQL_PORT = 3306
# Caminho do upload de arquivos
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__))+'/uploads'
