import sqlite3

# Função (def) quantidade de registros, qtd_registros

def qtd_registro():
    sql = "SELECT * from tb_cliente"  # Consulta a tabela tb_cliente
    cur.execute(sql)
    registros=cur.fetchall()        # registros é uma lista.
    #print(registros)
    qtd = len(registros)
    return qtd


conexao=sqlite3.connect('livraria.db') # Conexão com a base de dados livraria.db
cur=conexao.cursor()
print("Qtd =",qtd_registro())
sql="insert into tb_cliente(cpf, nome, idade) values(?,?,?)"
cpf1 = input('CPF; ')             # cpf1 = '423'
nome1 = input('Nome: ')           # nome1 = 'Ana'
idade1 = int(input('Idade: '))    # idade1 = 23
cur.execute(sql, (cpf1, nome1, idade1))
conexao.commit()
print ("one record added successfully")
v=qtd_registro()
print("Qtd = ", v)
cur.close()
conexao.close()