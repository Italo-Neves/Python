import sqlite3

conexao = sqlite3.connect('basedados.db')#cria o arquivo da base de dados
cursor = conexao.cursor()# cria o cursor que vai execultar os comando sql na base de dados

cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')
#cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?,?)', ('maria',50))
#ursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
#               {'id':'None', 'nome':'joão','peso':'80.5'}# criando uma tupla
#               )

conexao.commit()#executar o comoando acima
"""
cursor.execute(' UPDATE clientes SET nome =:nome WHERE id=:id',
               {'nome':'Joana','id': 2}
               )
conexao.commit()
"""

cursor.execute('DELETE FROM clientes where id=:id',
                    {'id':4}
               )

cursor.execute('SELECT * FROM clientes')
# fetchall == ele executa o comando e busca os valores da tabela cliente
#o for abaixo mostra o select
for linha in cursor.fetchall():
   identificado,nome,peso = linha
   print(identificado, nome, peso)


# é de bom costume fechar a conexão após utilizar a base de dados
cursor.close()
conexao.close()