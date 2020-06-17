import pymysql.cursors
from contextlib import  contextmanager
@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='localhost',
        user='Magnavox',
        password='testador',
        db='clientes',
        charset='utf8',
    )

    try:
        yield conexao#funciona como um return mas só pode ser usado em uma função
    finally:
        print('Conexão fechada')
        conexao.close()

with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql ='INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
        cursor.execute(sql,('Italo','Vinicius ',20,70))
        conexao.commit()


with conecta() as conexao:#gerenciador de contexto que está fechando a conexão
    with conexao.cursor() as cursor:#gerenciador de contexto que está fechando o cursor
        cursor.execute('SELECT * FROM clientes LIMIT 100')# é uma boa pratica limitar as pesquisas
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)