import sqlite3
conexao=sqlite3.connect('livraria.db') # Conexão com a base de dados livraria.db
cur=conexao.cursor()
sql = "SELECT * from tb_cliente"  # Consulta a tabela tb_cliente
cur.execute(sql)
registros=cur.fetchall()        # registros é uma lista.
print(type(registros))
if len(registros) > 0:
    # print(registros)  # Registros na horizontal
    ct = 0
    print('Consultando todos:')
    for registro in registros:
        print (registro)
        ct += 1
    print("Total de resistros: ", ct)
else:
    print('Lista vazia.')
cur.close()
conexao.close()