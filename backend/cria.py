import sqlite3

nome_banco = "granolastore.db"
con = sqlite3.connect(nome_banco)
cur = con.cursor()
# id INTEGER, modelo TEXT, cor TEXT, ano INTEGER, preco REAL, automatico INTEGER
produtos_loja = [
    (None, 'Vitoria Secret', 'Bolsa transversal', 'Branca', 'm', 2, 1700.0),
    (None, 'Louis Vuitton', 'Mochila de costa', 'Marrom', 'p', 3, 3500.0),
    (None, 'Victor Hugo', 'Transversal corrente', 'Preta', 'g', 5, 1300.0),
    (None, 'Louis Vuitton', 'Bolsa tiracolo', 'Preta', 'm', 5, 900.0),
    (None, 'Gucci', 'Bolsa transversal', 'Marrom', 'g', 4, 2500.0),
    (None, 'Bolsa Michael Kors', 'Transversal', 'Preta', 'p', 2, 1100.0)

]

cur.executemany("INSERT INTO produtos_loja VALUES (?, ?, ?, ?, ?, ?, ?)", produtos_loja)

con.commit()
con.close()
