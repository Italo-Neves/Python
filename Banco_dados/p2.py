import sqlite3

def qtd_registro():
    sql = "SELECT * from tb_cliente"  # Consulta a tabela tb_cliente
    cur.execute(sql)
    registros=cur.fetchall()        # registros é uma lista.
    #print(registros)
    qtd = len(registros)
    return qtd

# Inserir
conexao=sqlite3.connect('livraria.db') # Conexão com a base de dados livraria.db
cur=conexao.cursor()
sql="insert into tb_cliente(cpf, nome, idade) values('122', 'Paula', 21)"

#sql="insert into tb_cliente values('122', 'Paula', 21)"

cur.execute(sql)
conexao.commit()
print ("one record added successfully")
print('Qtd de registros = ', qtd_registro())   # Chamada da função
cur.close()
conexao.close()