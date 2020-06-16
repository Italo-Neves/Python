import sqlite3
database = 'livraria.db'
conexao=sqlite3.connect(database) # Criando a base de dados livraria.db e a conexão
cur =conexao.cursor()
# Criando a tabela tb_cliente dentro da base de dados livraira.db
cur.execute('''create table if not exists tb_cliente (
    cpf text,
    nome text,
    idade integer)''')
conexao.commit()
cur.close()
conexao.close()

