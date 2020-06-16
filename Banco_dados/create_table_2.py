import sqlite3
from sqlite3 import Error
def select_all():
    sql ="SELECT * from tb_livro"
    try:
        cur.execute(sql)
        registro = cur.fetchall()
        print('Consultando todos')
        for elemento in registro:
            print(elemento)
        print("Total deregistro: ",len(registro))
    except Error as e:
        print("menssagem de erro do selec_all")
        print(e)

def insert_one():
    sql ="insert into tb_livro(titulo,autor,preco,ano) values('java','Deitel','350.00','2014-06-08')"
    try:
        cur.execute(sql)
        conexao.commit()
        print("one record added successfully")
    except Error as e:
        print('Mensagem de erro no insert_one')
        print(e)
        conexao.rollback()
def update_one():
    pass
if __name__ == '__main__':
    database = 'livraria.db'
    conexao=sqlite3.connect(database) # Criando a base de dados livraria.db e a conexão
    try:
        cur =conexao.cursor()
        # Criando a tabela tb_cliente dentro da base de dados livraira.db
        cur.execute('''create table if not exists tb_livro (
            pk_idt integer primary key autoincrement,
            titulo text,
            autor text,
            preco float,
            ano text)
            ''')
        conexao.commit()
    except Error as e:
        print('Mensagem de erro no main')
        print(e)
        conexao.rollback()
        cur.close()
        conexao.close()
        exit(0)
    while True:
        opcao = int(input("[1] insert one\n[2] select all \n [3] update one\n [4] delete one\n[5] select one\n "
                          "[0] sair\n opção:"))
        if opcao ==1:
            insert_one()
        elif opcao ==2:
            select_all()
