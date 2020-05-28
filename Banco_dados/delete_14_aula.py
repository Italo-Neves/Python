import sqlite3

from Banco_dados.create_table_2 import cur


def qtd_registro():
    sql = "SELECT * from tb_cliente"
    cur.execute(sql)
    print(type(cur))
    registros = cur.fetchall()
    qtd = len(registros)
    return qtd
conexao=sqlite3.connect('livraria.db')
sql ="delete from tb_cliente where nome=?"
cur=conexao.cursor()
print('Qtd.',qtd_registro())

n = 'Carla'
cur.execute(sql,(n))