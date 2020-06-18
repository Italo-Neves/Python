from passlib.hash import pbkdf2_sha256 as cryp
import pymysql.cursors
from contextlib import contextmanager
#---------------------------------------------------- PESSOA -----------------------------------------------------------------------
class Pessoa:
    def __init__(self, nome, sobrenome, email, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def sobrenome(self):
        return self.__sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self.__sobrenome = sobrenome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    def nome_comleto(self):
        return f'{self.__nome} {self.__sobrenome}'

#---------------------------------------- USUÁRIO ----------------------------------------------------------------------
class Usuario(Pessoa):
    contador = 0
    @classmethod
    def conta_usuarios(cls):
        print(f'{cls.contador} usuário(s) no sistema.')

    def __init__(self, nome, sobrenome, email, cpf, senha, venda):
        super().__init__(nome, sobrenome, email, cpf)
        self.__venda = venda
        self.__id = Usuario.contador+1
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'\nUsuário criado: {self.__gera_usuario()}')

    @property
    def id(self):
        return self.__id

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def venda(self):
        return self.__venda

    @venda.setter
    def venda(self, venda):
        self.__venda = venda

    def checa_senha(self, senha):
        if cryp.verify(senha, senha):
            return True
        return False

    def __gera_usuario(self):
        return self.email.split('@')[0]

    def mostra_usuario(self,):
        print(f'\n {self.id}'
              f'\n Nome: {self.nome}'
              f'\n Sobrenome: {self.sobrenome}'
              f'\n CPF: {self.cpf}'
              f'\n E-mail: {self.email}')

#---------------------------------------- FUNCIONÁRIO ------------------------------------------------------------------
class Funcionario(Usuario):
    def __init__(self, nome, sobrenome, email, cpf, senha, funcao, venda):
        super().__init__(nome, sobrenome, email, cpf, senha, venda)
        self.__funcao = funcao

    @property
    def funcao(self):
        return self.__funcao

    def mostra_funcao(self):
        print(f'O Funcionário {Usuario.nome} realiza a função de {self.funcao}.')

#----------------------------------------  GERENTE ---------------------------------------------------------------------
class Gerente(Usuario):
    def __init__(self, nome, sobrenome, email, cpf, senha, setor, venda):
        super().__init__(nome, sobrenome, email, cpf, senha, venda)
        self.__setor = setor

    @property
    def setor(self):
        return self.__setor

    @setor.setter
    def setor(self, setor):
        self.__setor = setor

    def mostra_setor(self):
        print(f'O gerente {Usuario.nome} é responsável pelo setor {self.setor}.')

    def delUser(self):
        pass

#---------------------------------------- CLIENTE ----------------------------------------------------------------------
class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, email, cpf, compra):
        super().__init__(nome, sobrenome, email, cpf)
        self.__compra = compra

    @property
    def compra(self):
        return self.__compra

    def mostra_cliente(self):
        print(f'\n Nome: {self.nome}'
              f'\n Sobrenome: {self.sobrenome}'
              f'\n CPF: {self.cpf}'
              f'\n Email: {self.email}'
              f'\n Compra: {self.compra}')

#---------------------------------------- VENDA ------------------------------------------------------------------------
class Venda:
    def __init__(self, data, hora, cliente, vendedor):
        self.__data = data
        self.__hora = hora
        self.__cliente = cliente
        self.__vendedor = vendedor

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def hora(self):
        return self.__hora

    @hora.setter
    def hora(self, hora):
        self.__hora = hora

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def vendedor(self):
        return self.__vendedor

    @vendedor.setter
    def vendedor(self, vendedor):
        self.__vendedor = vendedor

    def carrinho_compras(self, estoque):
        carrinho = []
        produto = []
        c_preco = []
        s_preco = 0
        while produto != 'sair':
            print("Adicione um produto no carrinho ou digite 'sair': ")
            produto = input()
            if produto != 'sair':
                if produto == 'p1':
                    carrinho.append(p1.__dict__)
                    c_preco.append(p1.__dict__['_Produto__preco'])
                if produto == 'p2':
                    carrinho.append(p2.__dict__)
                    c_preco.append(p2.__dict__['_Produto__preco'])
                if produto == 'p3':
                    carrinho.append(p3.__dict__)
                    c_preco.append(p3.__dict__['_Produto__preco'])
                if produto == 'p4':
                    carrinho.append(p4.__dict__)
                    c_preco.append(p4.__dict__['_Produto__preco'])
                if produto == 'p5':
                    carrinho.append(p5.__dict__)
                    c_preco.append(p6.__dict__['_Produto__preco'])
                if produto == 'p6':
                    carrinho.append(p6.__dict__)
                    c_preco.append(p6.__dict__['_Produto__preco'])

        print(f'-------------------- Clagon Games --------------------'
              f'\nData: {self.data} Hora: {self.hora}'
              f'\n------------------------------------------------------'
              f'\nCliente: {self.cliente}'
              f'\n------------------------------------------------------')
        for produto in carrinho:
             print( f'\nProduto: {len(carrinho)} : {produto.values()}')
        for p in c_preco:
            s_preco += p
        print(f'\n------------------------------------------------------'
              f'\nTotal: {s_preco}'
              f'\n------------------------------------------------------')

#---------------------------------------- PRODUTO ----------------------------------------------------------------------
class Produto:
    contador = 0
    def __init__(self, nome, preco, codigo, descricao, pcusto, imposto):
        self.__nome = nome
        self.__preco = preco
        self.__codigo = codigo
        self.__descricao = descricao
        self.__pcusto = pcusto
        self.__imposto = imposto

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def pcusto(self):
        return self.__pcusto

    @pcusto.setter
    def pcusto(self, pcusto):
        self.__pcusto = pcusto

    @property
    def imposto(self):
        return self.__imposto

    @imposto.setter
    def imposto(self, imposto):
        self.__imposto = imposto

    def lucro(self, imposto, preco, pcusto):
        pimposto = pcusto * imposto/100
        lucro = (pimposto + pcusto) - preco
        return lucro

    def desconto(self, preco):
        vdesc = int(input('Digite o valor do desconto'))
        desc = (preco * vdesc/100) - preco
        return f'O desconto foi de {desc}.'

    def mostra_produto(self):
        print(f'\nNome: {self.nome}'
              f'\nCódigo: {self.codigo}'
              f'\nPreço: {self.preco}'
              f'\nDescrição: {self.descricao}'
              f'\nPreço de custo: {self.pcusto}'
              f'\nPorcentagem de impostos: {self.imposto}%')

#---------------------------------------- CRUD -------------------------------------------------------------------------

@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='localhost',
        user='Magnavox',
        password='testador',
        db='Eletronica',
        charset='utf8',
    )
    try:
        yield conexao  # funciona como um return mas só pode ser usado em uma função
    finally:
        print('Conexão fechada')
        conexao.close()

def menu():
    print(f'\nO deseja fazer?\n'
        f'\n1 - Cadastrar produto'
        f'\n2 - Cadastrar usuário'
        f'\n3 - Cadastrar cliente'
        f'\n4 - Alterar produto'
        f'\n5 - Alterar usuário'
        f'\n6 - Alterar cliente'
        f'\n7 - Visualizar produto'
        f'\n8 - Visualizar usuário'
        f'\n9 - Visualizar cliente'
        f'\n10 - Deletar produto'
        f'\n11 - Deletar usuário'
        f'\n12 - Deletar cliente')
    opcao = input('\nDigite o número da operação: ')
    return opcao

def cadastra_produto():
    nome = input('\nNome do produto: ')
    preco = int(input('Valor do produto: R$ '))
    codigo = int(input('Código de barras: '))
    descricao = input('Descrição do produto: ')
    pcusto = int(input('Valor de fábrica: R$ '))
    imposto = int(input('Porcentagem de impostos: '))

    with conecta() as conexao:
        with conexao.cursor() as cursor:
            sql = 'INSERT INTO TB_produto (PK_codigo, nome, descricao, pcusto, pvenda, imposto) VALUES (%s, %s, %s, %s, %s, %s)'
            cursor.execute(sql, (codigo,nome, descricao, pcusto, preco, imposto))
            conexao.commit()

def altera_produto(codigo):
    print('\nO que deseja alterar?'
          '\n [1] - Atualizar nome'
          '\n [2] - Atualizar preço'
          '\n [3] - Atualizar descrição'
          '\n [4] - Atualizar valor de fábrica'
          '\n [5] - Atualizar impostos')
    op = input('\nDigite o número da operação: ')
    if op == '1':
        nome = input('Digite o novo nome')
        with conecta() as conexao:
            with conexao.cursor() as cursor:
                sql = 'UPDATE TB_produtos SET nome=%s WHERE PK_codigo=%s'
                cursor.execute(sql, (nome ,codigo))
                conexao.commit()

    if op == '2':
        preco = input(float('Digite o novo preço'))
        with conecta() as conexao:
            with conexao.cursor() as cursor:
                sql = 'UPDATE TB_produtos SET pvenda=%s WHERE PK_codigo=%s'
                cursor.execute(sql, (preco ,codigo))
                conexao.commit()

    if op == '3':
        descricao = input('Digite a nova descrição')
        with conecta() as conexao:
            with conexao.cursor() as cursor:
                sql = 'UPDATE TB_produtos SET descricao=%s WHERE PK_codigo=%s'
                cursor.execute(sql, (descricao ,codigo))
                conexao.commit()
    if op == '4':
        pcusto = input('Digite o novo preço de fábrica')
        with conecta() as conexao:
            with conexao.cursor() as cursor:
                sql = 'UPDATE TB_produtos SET pcusto=%s WHERE PK_codigo=%s'
                cursor.execute(sql, (pcusto ,codigo))
                conexao.commit()
    if op == '5':
        imposto = input('Digite a nova taxa de imposto')
        with conecta() as conexao:
            with conexao.cursor() as cursor:
                sql = 'UPDATE TB_produtos SET imposto=%s WHERE PK_codigo=%s'
                cursor.execute(sql, (imposto ,codigo))
                conexao.commit()

def cadastra_usuario():
    su = input('\n [1] - Gerente'
               '\n [2] - Funcionário'
               '\n Qual a opção desejada? ')
    if su =='1':
         nome = input('\nInforme o nome: ')
         sobrenome =input('Informe o sobrenome: ')
         email = input('Informe o e-mail: ')
         cpf = input('Informe o CPF: ')
         senha = input('Informe a senha: ')
         confirma_senha = input('Confirme a senha: ')
         setor = input('Setor: ')
         venda = 0

         if senha == confirma_senha:
            user = Gerente(nome, sobrenome, email, cpf, senha, setor, venda)
            print(f'\nGerente {user.nome_comleto()} criado com sucesso!\n')
            print(user.__dict__)
            return user.__dict__
         else:
            print('Senha incorreta!')
            exit(42)
    if su =='2':

        if su == '2':
            nome = input('\nInforme o nome: ')
            sobrenome = input('Informe o sobrenome: ')
            email = input('Informe o e-mail: ')
            cpf = input('Informe o CPF: ')
            senha = input('Informe a senha: ')
            confirma_senha = input('Confirme a senha: ')
            cargo = input('Cargo: ')
            venda = 0

            if senha == confirma_senha:
                user = Funcionario(nome, sobrenome, email, cpf, senha, cargo, venda)
                print(f'\nFuncionário {user.nome_comleto()} criado com sucesso!\n')
                print(user.__dict__)
                return user.__dict__
            else:
                print('\nSenha incorreta!')
                exit(42)

    else:
        print('Opção inválida!')

def realiza_venda():
    data = input('Data: ')
    hora = int(input('Horário: '))
    cliente = input('Cliente: ')
    vendedor = int(input('Vendedor: '))

    venda = Venda(data, hora, cliente, vendedor)
    print(f'Venda iniciada!')
    print(venda.__dict__)

def cadastra_cliente():
    nome = input('\nInforme o nome: ')
    sobrenome = input('Informe o sobrenome: ')
    email = input('Informe o e-mail: ')
    cpf = input('Informe o CPF: ')
    compra = 0
    c = Cliente(nome, sobrenome, email, cpf, compra)
    print(f'\nCliente {c.nome_comleto()} cadastrado com sucesso!\n')
    print(c.__dict__)
    return c.__dict__

def altera_cliente(c):
    print('\nO que deseja alterar?'
          '\n [1] - Atualizar nome'
          '\n [2] - Atualizar sobrenome'
          '\n [3] - Atualizar e-mail'
          '\n [4] - Atualizar CPF')
    op = input('\nDigite o número da operação: ')
    if op == '1':
       nnome = (input('\nDigite o novo nome: '))
       c['_Pessoa__nome'] = nnome
    if op == '2':
       nsobrenome = (input('\nDigite o novo sobrenome: '))
       c['_Pessoa__sobrenome'] = nsobrenome
    if op == '3':
       nemail = (input('\nDigite o novo e-mail: '))
       c['_Pessoa__email'] = nemail
    if op == '4':
       ncpf = (input('\nDigite o novo CPF: '))
       c['_Pessoa__cpf'] = ncpf

def visualiza_usuario(user):
    Usuario.mostra_usuario(user)

def visualiza_produto():
    with conecta() as conexao:  # gerenciador de contexto que está fechando a conexão
        with conexao.cursor() as cursor:  # gerenciador de contexto que está fechando o cursor
            cursor.execute('SELECT * FROM TB_produto LIMIT 100')  # é uma boa pratica limitar as pesquisas
            resultado = cursor.fetchall()

            for linha in resultado:
                print(linha)

def visualiza_cliente(user):
    Cliente.mostra_cliente(user)

def delete_usuario(func):
    f = input('\nQual funcionário será deletado? ')
    if f in func:
        func.pop(f)
        print(f'\nFuncionário deletado!')

def delete_cliente(c_cadastrados):
    c = input('\nQual cliente será deletado? ')
    if c in c_cadastrados:
        c_cadastrados.pop(c)
        print(f'Cliente deletado!')

def delete_produto(codigo):
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            sql = 'DELETE FROM TB_produtos WHERE PK_codigo = %s'
            cursor.execute(sql,(codigo,))
            conexao.commit()



if __name__ == '__main__':
#---------------------------------------- PRODUTOS ---------------------------------------------------------------------
   p1 = Produto('Mousepad', 69.90, 789001, 'Mouse pad com apoio para a mão', 35, 100)
   p2 = Produto('Teclado', 499.90, 789002, 'Teclado mecânico ', 200, 150)
   p3 = Produto('Mouse', 179.90, 789003, 'Mouse óptico sem fio', 50, 260)
   p4 = Produto('Monitor', 1299.90, 789004, 'Monitor AOC Hero PF2460', 700, 100)
   p5 = Produto('Gabinete', 249.90, 789005, 'Gabinete mid tower', 100, 150)
   p6 = Produto('Microfone', 59.90, 789006, 'Microfone de mesa', 20, 200)
#---------------------------------------- USUÁRIOS ---------------------------------------------------------------------
   g1 = Gerente('Italo', 'Vinicius', 'italo@gmail.com', '12345678901', '123456', 'Vendedor', 0)
   f1 = Funcionario('João', 'Batista', 'joao@gmail.com', '12345678902', '654321', 1, 0)
#---------------------------------------- CLIENTES ---------------------------------------------------------------------
   c1 = Cliente('Juliana', 'Pereira', 'juliana@gmail.com', '12345678903', 0)
#----------------------------------------------Vendas----------------------------------------------------------------
   v1 = Venda('21/05/2020', '08:12', c1.__dict__['_Pessoa__nome'], f1)
#--------------------------------------------------------------------------------------------------------
   estoque = [p1.__dict__, p2.__dict__, p3.__dict__, p4.__dict__, p5.__dict__, p6.__dict__]
   func = [f1.__dict__, g1.__dict__]
   c_cadastrados = [c1.__dict__]
#---------------------------------------- MENU -------------------------------------------------------------------------
   while True:
       r = menu()
       if r == '1':
           try:
               cadastra_produto()
           except:
               print('Erro ao cadastrar, por favor tente mais tarde!')
#-----------------------------------------------------------------------------------------------------------------------
       if r == '2':
           try:
               func.append(cadastra_usuario())
           except:
               print('Erro ao cadastrar, por favor tente mais tarde!')
#-----------------------------------------------------------------------------------------------------------------------
       elif r == '3':
           try:
               c_cadastrados.append(cadastra_cliente())
           except:
               print('Erro ao cadastrar, por favor tente mais tarde!')
#-----------------------------------------------------------------------------------------------------------------------
       elif r == '4':
            c = input(int('Digite o código do produto que dejesa altearar'))
            altera_produto(c)
#-----------------------------------------------------------------------------------------------------------------------
       elif r == '5':
           opau = input('\nQual usuário deseja alterar? ')
           if opau in func:
               print('\nErro 404')
           else:
               opu = input('\nUsuário não cadastrado, deseja cadastrá-lo? ').upper()
               if opu == 'S':
                   cadastra_usuario()
#-----------------------------------------------------------------------------------------------------------------------
       elif r == '6':
           continua = True
           while continua:
               c = 0
               opcao = input('\nDigite o nome do Cliente: ')
               for i in c_cadastrados:
                   if c_cadastrados[c]['_Pessoa__nome'] == opcao:
                       print(i)
                       altera_cliente(i)
                       print(i)
                       continua = input('\nDeseja continuar? ').upper()
                       if continua == 'S':
                           continua = True
                       else:
                           continua = False
                   else:
                       c += 1
                       if c > len(c_cadastrados):
                           break
                   if i not in c_cadastrados:
                       opp = input('Cliente não cadastrado, deseja cadastrá-lo? ').upper()
                       if opp == 'S':
                           cadastra_cliente()
#-----------------------------------------------------------------------------------------------------------------------
       elif r == '7':
           opvp1 = input('\n [1] - Mostrar produto especifico'
                         '\n [2] - Mostrar Todos os produtos'
                         '\n Digite a opção desejada: ')
           if opvp1 == '1':
               continua = True
               while continua:
                   c = 0
                   opcao = input('\nDigite o nome do produto: ')
                   for i in estoque:
                       if estoque[c]['_Produto__nome'] == opcao:
                           print(estoque[c])
                           continua = False
                           break
                       else:
                           c += 1
                           if c > len(estoque):
                               break
           if opvp1 == '2':
               visualiza_produto()
#-----------------------------------------------------------------------------------------------------------------------
       elif r == '8':
           opvp1 = input('\n [1]-Mostrar usuário especifico'
                         '\n [2]-Mostrar todos os usuários'
                         '\n Digite a opção desejada: ')
           if opvp1 == '1':
               continua = True
               while continua:
                   c = 0
                   opcao = input('\nDigite o nome do usuário: ')
                   for i in func:
                       if func[c]['_Pessoa__nome'] == opcao:
                           print(i)
                           continua = False
                           break
                       else:
                           c += 1
                           if c > len(func):
                               if i not in func:
                                   opu = input('\nUsuário não cadastrado, deseja cadastrá-lo?').upper()
                                   if opu == 'S':
                                       cadastra_usuario()
                           break

           if opvp1 == '2':
               for u in func:
                   print(u)
#-----------------------------------------------------------------------------------------------------------------------
       elif r == '9':
           opvc1 = input('\n [1]-Mostrar cliente específico'
                         '\n [2]-Mostrar todos os clientes'
                         '\n Digite a opção desejada: ')
           if opvc1 == '1':
               continua = True
               opcao = input('\nDigite o nome do cliente: ')
               c = 0
               for i in c_cadastrados:
                   if c_cadastrados[c]['_Pessoa__nome'] == opcao:
                       print(i)
                       continua = False
                       break
                   opc = input('\nCliente não cadastrado, deseja cadastrá-lo? ').upper()
                   if opc == 'S':
                       cadastra_cliente()
                       break
           if opvc1 == '2':
               pass
#-----------------------------------------------------------------------------------------------------------------------
       elif r == '10':
           p = input (int('Digite o código do produto a ser excluido'))
           delete_produto(p)
#-----------------------------------------------------------------------------------------------------------------------
       elif r == '11':
           delete_usuario(func)
#-----------------------------------------------------------------------------------------------------------------------
       elif r == '12':
           delete_cliente(c_cadastrados)
#-----------------------------------------------------------------------------------------------------------------------
       elif r == 'sair':
           break