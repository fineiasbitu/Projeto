import sqlite3 # importa o módulo sqlite3
import os.path # importa o módulo os.path, para usar a exists()
import os      # importa o módulo os, para usar a unlink()

nome_banco = "granolastore.db"

if os.path.exists(nome_banco): # Exclui o arquivo caso ele exista
    os.unlink(nome_banco)

conexao = sqlite3.connect(nome_banco) # Conecta no banco
cursor = conexao.cursor() # Obtém o cursor para o banco

consulta = """CREATE TABLE produtos_loja (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    modelo TEXT,
    cor TEXT,
    tamanho INTEGER,
    quantidade REAL,
    preco REAL,
    )
    """
cursor.execute(consulta) # Executa a consulta SQL
conexao.close() # Fecha a conexão com o banco
