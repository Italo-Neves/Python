import sqlite3
# Função (def) quantidade de registros, qtd_registros
def qtd_registro():
    sql = "SELECT * from tb_cliente"  # Consulta a tabela tb_cliente
    cur.execute(sql)
    registros=cur.fetchall()        # registros é uma lista.
    #print(registros)
    qtd = len(registros)
    return qtd

# Inserir vários usando lista
conexao=sqlite3.connect('livraria.db') # Conexão com a base de dados livraria.db
cur=conexao.cursor()
sql="insert into tb_cliente(cpf, nome, idade) values(?,?,?)"
lista_cliente=[
    ('123', 'Paulo', 31),
    ('555','Lucia', 22)
]   # lista

cur.executemany(sql, lista_cliente)            # Com lista usa o executemany
conexao.commit()
print ("records added successfully")
print("Qtd de registros = ", qtd_registro())
cur.close()
print("Fecha a base de dados db")
conexao.close()