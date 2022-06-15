
import sqlite3
from flask import Flask, jsonify
from flask_cors import CORS


def pega_conexao():
    nome_banco = "granolastore.db"
    con = sqlite3.connect(nome_banco) # Conecta no banco
    return con

# Aplicação web com Flask
app = Flask(__name__)
CORS(app)

@app.route("/")
def raiz():
    return "Resposta do meu backend em Python!"

@app.route("/todos")
def todos():
    con = pega_conexao()
    cur = con.cursor()

    try: 
       cur.execute("SELECT * FROM produtos_loja")
    except:
       con.close()
       return jsonify("Erro ao consultar o banco") 
       
    dados = cur.fetchall()
    con.close()
    return jsonify(dados)

@app.route("/lista/<int:id>") # http://127.0.0.1:5000/lista/1
def lista_um(id):
    con = pega_conexao()
    cur = con.cursor()

    try:
        cur.execute(f"SELECT * FROM produtos_loja WHERE id={id}")
    except:
        con.close()
        return jsonify("Erro ao buscar no banco")
    dados = cur.fetchone()
    con.close()
    return jsonify(dados)

app.run()

# Flask + Python + SQLite

    
 