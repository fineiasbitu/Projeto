import sqlite3

nome_banco = "granolastore.db"
con = sqlite3.connect(nome_banco)
cur = con.cursor()
# id INTEGER, modelo TEXT, cor TEXT, ano INTEGER, preco REAL, automatico INTEGER
produtos_loja = [
    (None, 'vitoria secret', 'bolsa transversal', 'branca', 'm', 2, 1.700),
    (None, 'louis vuitton', 'mochila de costa', 'marron', 'p', 3, 3.50),
    (None, 'victor hugo', 'transversal corrente', 'preta', 'g', 5, 600)
]

cur.executemany("INSERT INTO produtos_loja VALUES (?, ?, ?, ?, ?, ?)", produtos_loja)

con.commit()
con.close()
