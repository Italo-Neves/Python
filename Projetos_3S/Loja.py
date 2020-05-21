from passlib.hash import pbkdf2_sha256 as cryp #importando o necessario para criptografia char256
"""
Simas precisa de um sistema de controle de caixa para a sua loja de eletronicos
"""

#-----------------------------------------Pessoa---------------------------------------------------------------------------------------------------
class Pessoa:
    def __init__(self, nome, sobrenome, email,cpf):
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

#---------------------------------------------Usuario---------------------------------------------------------------------------------------------------
class Usuario(Pessoa):
    contador = 0
    @classmethod # e necessario para criar um método de classe
    def conta_usuarios(cls):# o parametor é a propria classe
        print(f'{cls.contador} usuario(s) no sistema')


    def __init__(self, nome, sobrenome, email, cpf, senha, venda):
        super().__init__(nome,sobrenome, email, cpf)
        self.__venda = venda
        self.__id = Usuario.contador+1
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)# qual string sera incriptada, o ronund mostra quantos embaralhamentos seram feitos salt = parte do texto que será juntada
        Usuario.contador = self.__id
        print(f'Usuario criado: {self.__gera_usuario()}')

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

    #verifica se a senha digitada é igual a senha registrada
    def checa_senha(self,senha):
        if cryp.verify(senha, senha):
            return True
        return False


    def __gera_usuario(self):
        return self.email.split('@')[0]
        #quebra a string no ponto desejado e devolve o que estava antes do parametro na posiçãozeroda lista

    def mostra_usuario(self,):
        print(f'\n {self.id}'
              f'\n Nome:{self.nome}'
              f'\n Sobrenome:{self.sobrenome}'
              f'\n CPF:{self.cpf}'
              f'\n Email:{self.email}')

#--------------------------------------------Funcionario---------------------------------------------------------------------------------------------------
class Funcionario(Usuario):
    def __init__(self, nome, sobrenome, email, cpf, senha, funcao, venda):
        super().__init__(nome,sobrenome, email, cpf, senha, venda)
        self.__funcao = funcao

    @property
    def funcao(self):
        return self.__funcao

    def mostra_funcao(self):
        print(f'O Funcionario {Usuario.nome} realiza a função de {self.funcao}')

#---------------------------------------------Gerente---------------------------------------------------------------------------------------------------
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
        print(f'O gerente:{Usuario.nome} e responsavel pelo setor:{self.setor}')

    def delUser(self):
        pass

#---------------------------------------------Cliente---------------------------------------------------------------------------------------------------
class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, email, cpf, compra):
        super().__init__(nome, sobrenome, email, cpf)
        self.__compra = compra

    @property
    def compra(self):
        return self.__compra

    def mostra_cliente(self):
        print(f'\n Nome:{self.nome}'
              f'\n Sobrenome:{self.sobrenome}'
              f'\n CPF:{self.cpf}'
              f'\n Email:{self.email}'
              f'\n Compra:{self.compra}')

#-----------------------------------------------Venda---------------------------------------------------------------------------------------------------
class Venda:
    def __init__(self, data, hora,  cliente, vendedor):
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

    def carrinho_compras(self,estoque):
        carrinho = []
        produto = []
        c_preco = []#contador de precos
        s_preco = 0
        while produto != 'sair':
            print("Adicione um produto no carrinho ou digite 'sair para sair:'")
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

        print(f'----------------Eletronica Simas Turbo--------------------'
              f'\nData:{self.data} Hora:{self.hora}'
              f'\n--------------------------------------------------------'
              f'\nCliente:{self.cliente}'
              f'\n--------------------------------------------------------')
        for produto in carrinho:
             print( f'\n Produto: {len(carrinho)}:{produto.values()}')
        for p in c_preco:
            s_preco += p
        print(f'\n--------------------------------------------------------'
              f'\nTotal:{s_preco}'
              f'\n--------------------------------------------------------')

#----------------------------------------------Produto---------------------------------------------------------------------------------------------------
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

    def lucro(self,imposto, preco, pcusto):
        pimposto = pcusto * imposto/100
        lucro = (pimposto + pcusto) - preco
        return  lucro

    def desconto(self, preco):
        vdesc = int(input('Digite o valor do desconto'))
        desc = (preco * vdesc/100) - preco
        return f'O deconto foi de {desc}'




    def mostra_produto(self):
        print(f'\n Nome:{self.nome}'
              f'\n Código:{self.codigo}'
              f'\n Preço:{self.preco}'
              f'\n Descrição:{self.descricao}'
              f'\n Preço de custo:{self.pcusto}'
              f'\n Porcentagem de impostos:{self.imposto}%')
#------------------------------------------------CRUD----------------------------------------------------------------------


def menu():
    print(f'O deseja fazer?'
        f'\n1 - Cadastrar produto'
        f'\n2 - Cadastrar usuario'
        f'\n3 - Cadastrar cliente'
        f'\n4 - Alterar produto'
        f'\n5 - Alterar usuario'
        f'\n6 - Alterar cliente'
        f'\n7 - visualizar produto'
        f'\n8 - visualizar usuario'
        f'\n9 - visualizar cliente'
        f'\n10 - Deleta produto'
        f'\n11 - Deleta usuario'
        f'\n12 - Deleta cliente')
    opcao = input('\nDigite o número da operção')
    return opcao

def cadastra_produto():
    nome = input('Nome do produto: ')
    preco = int(input('Valor do produto: '))
    codigo = int(input('Código de barras: '))
    descricao = input('Descrição do produto: ')
    pcusto = int(input('valor de fabrica: '))
    imposto = int(input('Porcentagem de impostos: '))

    p = Produto(nome, preco, codigo, descricao, pcusto, imposto)
    print(f'O produto {p.nome} foi cadastrado com sucesso!')
    print(p.__dict__)
    return p.__dict__

def altera_produto(c):
    print('O que deseja alterar?'
          '\n 1 - Atualizar nome'
          '\n 2 - Atualizar preço'
          '\n 3 - Atualizar codigo de barras'
          '\n 4 - Atualizar descrição'
          '\n 4 - Atualizar valor de fabrica'
          '\n 4 - Atualizar impostos')
    op = input('Digite o número da operação')
    if op == '1':
       nnome = (input('Digite o novo nome'))
       c['_Produto__nome'] = nnome
    if op == '2':
       ncodigo = (input('Digite o preço'))
       c['_Produto__codigo'] = ncodigo
    if op == '3':
       npreco = (input('Digite o codigo de barras'))
       c['_Produto__preco'] = npreco
    if op == '4':
       ndescricao = (input('Digite a nova descrição'))
       c['_Produto__descricao'] = ndescricao
    if op == '5':
       npcusto = (input('Digite o novo preço de fabrica'))
       c['_Produto__pcusto'] = npcusto
    if op == '6':
       nimposto = (input('Digite a nova porcentagem de impostos'))
       c['_Produto__imposto']= nimposto

def cadastra_usuario():
    su = input('\n 1 - Gerente'
               '\n 2 - Funcionario')
    if su =='1':
         nome = input('Informe o nome: ')
         sobrenome =input('Informe o sobrenome: ')
         email = input('Informe o e-mail: ')
         cpf = input('Informe o CPF: ')
         senha = input('Informe a senha: ')
         confirma_senha = input('Confirme a senha: ')
         setor = input('Setor: ')
         venda = 0

         if senha == confirma_senha:
            user = Gerente(nome, sobrenome, email, cpf, senha, setor, venda)
            print(f'Usuário {user.nome_comleto()} criado com sucesso!')
            print(user.__dict__)
            return user.__dict__
         else:
            print('Senha não confere...')
            exit(42)
    if su =='2':

        if su == '2':
            nome = input('Informe o nome: ')
            sobrenome = input('Informe o sobrenome: ')
            email = input('Informe o e-mail: ')
            cpf = input('Informe o CPF: ')
            senha = input('Informe a senha: ')
            confirma_senha = input('Confirme a senha: ')
            cargo = input('Cargo: ')
            venda = 0

            if senha == confirma_senha:
                user = Funcionario(nome, sobrenome, email, cpf, senha, cargo, venda)
                print(f'Usuario {user.nome_comleto()} criado com sucesso!')
                print(user.__dict__)
                return user.__dict__
            else:
                print('Senha não confere...')
                exit(42)

    else:
        print('Opção inválida!')

def realiza_venda():
    data = input('Digite a data: ')
    hora = int(input('Horario: '))
    cliente = input('Cliente: ')
    vendedor = int(input('Vendedor: '))

    venda = Venda(data, hora, cliente, vendedor)
    print(f'Venda iniciada!')
    print(venda.__dict__)

def cadastra_cliente():
    nome = input('Informe o nome: ')
    sobrenome = input('Informe o sobrenome: ')
    email = input('Informe o email: ')
    cpf = input('Informe o cpf: ')
    compra = 0
    c = Cliente(nome, sobrenome, email, cpf, compra)
    print(f'Cliente {c.nome_comleto()} criado com sucesso!')
    print(c.__dict__)
    return c.__dict__

def altera_cliente(c):
    print('O que deseja alterar?'
          '\n1 - Atualizar nome'
          '\n2 - Atualizar sobrenome'
          '\n3 - Atualizar e-mail'
          '\n4 - Atualizar CPF')
    op = input('Digite o número da operação')
    if op == '1':
       nnome = (input('Digite o novo nome'))
       c['_Pessoa__nome'] = nnome
    if op == '2':
       nsobrenome = (input('Digite o novo sobrenome'))
       c['_Pessoa__sobrenome'] = nsobrenome
    if op == '3':
       nemail = (input('Digite o novo e-mail'))
       c['_Pessoa__email'] = nemail
    if op == '4':
       ncpf = (input('Digite o novo CPF'))
       c['_Pessoa__cpf'] = ncpf

def visualiza_usuario(user):
    Usuario.mostra_usuario(user)

def visualiza_produto(produto):
    Produto.mostra_produto(produto)

def visualiza_cliente(user):
    Cliente.mostra_cliente(user)

def delete_usuario(func):
    f = input('Qual funcionario será deletado?')
    if f in func:
        func.pop(f)
        print(f'Funcionario deletado!')

def delete_cliente(c_cadastrados):
    c = input('Qual cliente será deletado?')
    if c in c_cadastrados:
        c_cadastrados.pop(c)
        print(f'Produto deletado!')

def delete_produto(estoque):
    item = input('Qual produto será deletado?')
    if item in estoque:
        estoque.pop(item)
        print(f'Produto deletado!')

if __name__ == '__main__':
#----------------------------------------------Produtos-------------------------------------------------------
   p1 = Produto('Mousepad', 10.99, 7891099, 'Mouse pad com apoio para a mão', 2.49, 1)
   p2 = Produto('Teclado', 299.99, 78929999, 'Teclado mecanico ', 2.49, 2)
   p3 = Produto('Mouse', 89.99, 7898999, 'Mouse optico sem fio', 2.49, 3)
   p4 = Produto('Monitor', 499.99, 789499.99, 'Monitor asus 1400X900', 2.49, 1)
   p5 = Produto('Gabinete', 199.99, 78919999, 'gabinete grande', 2.49, 1)
   p6 = Produto('Microfone', 59.99, 7895999, 'Microfone de mesa', 2.49, 2)
#---------------------------------------------Usuarios---------------------------------------------------------
   g1 = Gerente('Italo', 'Vinicius', 'chefe@gmail.com', '12345678945', '123456', 'Vendedor', 0)
   f1 = Funcionario('João', 'Batista', 'jao@gmail.com', '65478932145', '789456', 1, 0)
#---------------------------------------------Clientes----------------------------------------------------------
   c1 = Cliente('Juliana', 'Pereira', 'ju@gmail.com', '45696325814', 0)
#----------------------------------------------Vendas----------------------------------------------------------------
   v1 = Venda('20/05/2020', '13:50', c1.__dict__['_Pessoa__nome'], f1)
#--------------------------------------------------------------------------------------------------------
   estoque = [p1.__dict__, p2.__dict__, p3.__dict__, p4.__dict__, p5.__dict__, p6.__dict__]
   func = [f1.__dict__, g1.__dict__]
   c_cadastrados = [c1.__dict__]

# #-------------------------------------------------------Menu--------------------------------------------------------
   while True:
       r = menu()
       if r == '1':
           try:
               estoque.append(cadastra_produto())
           except:
               print('Erro ao cadastrar, por favor tente mais tarde!')
#------------------------------------------------------------------------------------------------------
       if r == '2':
           try:
               func.append(cadastra_usuario())
           except:
               print('Erro ao cadastrar, por favor tente mais tarde!')
#------------------------------------------------------------------------------------------------------
       elif r == '3':
           try:
               c_cadastrados.append(cadastra_cliente())
           except:
               print('Erro ao cadastrar, por favor tente mais tarde!')
#------------------------------------------------------------------------------------------------------
       elif r == '4':
           continua = True
           while continua:
               c = 0
               opcao = input('Digite o nome do produto')
               for i in estoque:
                   if estoque[c]['_Produto__nome'] == opcao:
                       altera_produto(i)
                       print(i)
                       continua = input('Deseja continuar?').upper()
                       if continua == 'S':
                           continua = True
                       else:
                           continua = False
                   else:
                       c += 1
                       if c > len(estoque):
                           break
                   if i not in estoque:
                       opp = input('Produto não cadastrado, deseja cadastra-lo?').upper()
                       if opp == 'S':
                           cadastra_produto()
#------------------------------------------------------------------------------------------------------
       elif r == '5':
           opau = input('Qual usuario deseja alterar?')
           if opau in func:
               print('Erro 400')
           else:
               opu = input('Usuario não cadastrado, deseja cadastra-lo?').upper()
               if opu == 'S':
                   cadastra_usuario()
#------------------------------------------------------------------------------------------------------
       elif r == '6':
           continua = True
           while continua:
               c = 0
               opcao = input('Digite o nome do Cliente')
               for i in c_cadastrados:
                   if c_cadastrados[c]['_Pessoa__nome'] == opcao:
                       altera_cliente(i)
                       print(i)
                       continua = input('Deseja continuar?').upper()
                       if continua == 'S':
                           continua = True
                       else:
                           continua = False
                   else:
                       c += 1
                       if c > len(c_cadastrados):
                           break
                   if i not in c_cadastrados:
                       opp = input('Cliente não cadastrado, deseja cadastra-lo?').upper()
                       if opp == 'S':
                           cadastra_cliente()
#------------------------------------------------------------------------------------------------------
       elif r == '7':
           opvp1 = input('\n [1]-Mostrar produto especifico'
                         '\n [2]-Mostrar Todos os produtos')
           if opvp1 == '1':
               continua = True
               while continua:
                   c = 0
                   opcao = input('Digite o nome do produto')
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
               for p in estoque:
                   print(p)
#------------------------------------------------------------------------------------------------------
       elif r == '8':
           opvp1 = input('\n [1]-Mostrar usuario especifico'
                         '\n [2]-Mostrar Todos os usuarios')
           if opvp1 == '1':
               opvp2 = input('Qual usuario deseja visualizar?')
               if opvp2 in estoque:
                    visualiza_usuario(opvp2)
               else:
                   opu = input('Usuario não cadastrado, deseja cadastra-lo?').upper()
                   if opu == 'S':
                       cadastra_usuario()

           if opvp1 == '2':
               for u in func:
                   print(u)
#------------------------------------------------------------------------------------------------------
       elif r == '9':
           opvc1 = input('\n [1]-Mostrar cliente especifico'
                         '\n [2]-Mostrar Todos os cliente')
           if opvc1 == '1':
               opcao = input('Digite o nome do Cliente')
               c = 0
               for i in estoque:
                   if estoque[c]['_Pessoa__nome'] == opcao:
                       print(i.__dict__)
                   opc = input('Cliente não cadastrado, deseja cadastra-lo?').upper()
                   if opc == 'S':
                       cadastra_cliente()
           if opvc1 == '2':
               for c in c_cadastrados:
                   print(c)
#--------------------------------------------------------------------------------------------------------------------
       elif r == '10':
           delete_produto(estoque)
#-------------------------------------------------------------------------------------------------------------------------
       elif r == '11':
           delete_usuario(func)
#------------------------------------------------------------------------------------------------------------------
       elif r == '12':
           delete_cliente(c_cadastrados)
#------------------------------------------------------------------------------------------------------------------------------
       elif r == 'sair':
           break