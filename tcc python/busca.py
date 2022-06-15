import sqlite3


nome_banco = "granolastore.db"
con = sqlite3.connect(nome_banco)
cur = con.cursor()
#id INTEGER, modelo TEXT, cor TEXT, ano INTEGER, preco REAL

#sql = "SELECT modelo, preco FROM Carros WHERE modelo LIKE '%P%
sql = "SELECT * FROM produtos_loja" #SELECT <CAMPOS> FROM <TABELA>
cur.execute(sql)
dados = cur.fetchall()

for e in dados:
    print(e)

con.close()