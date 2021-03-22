"""   CEUB   -   Ciência da Computação   -   Prof. Barbosa
Atalho de teclado: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha

- Composição
No programa anterior, usamos agregação. Agora, a classe Conta tem um Cliente e associamos
estas duas classes. Mas, a classe Cliente existe independente da classe Conta.
Agora, a Conta possui um histórico, contendo a data de abertura da conta e
suas transações. Crie uma classe para representar o histórico:

- Composição
Quando a existência de uma classe depende de outra classe, como é a relação da
classe Histórico com a classe Conta, dizemos que a classe Historico compõe a classe Conta.

- Implemente:
1- Crie a classe Historico com os atributos data/hora de abertura da conta e transações realizadas.
- Crie o método get para retornar a data/hora da abertura da conta.
- Crie o método get para retornar o historico da conta.
- Modifique a classe Conta de modo que ela tenha um historico. Diferente da relação do
  cliente com uma conta, a existência de um histórico depende da existência de uma Conta
  Ou seja, acrescente o atributo historico que recebe um objeto da classe Historico.
5- Altere o método deposito, ele deve armazenar as informações da transação no histórico
- Cria o objeto conta1, faça um depósito e mostre o histórico
- Na classe Historico, crie o método para mostrar o histórico da conta:
  depósitos, saques, transferência e extratos
8- Altere o método sqque, ele deve armazenar as informações da transação no histórico, teste.
- Altere o método extrato, ele deve armazenar as informações da transação no histórico, teste.
10- Altere o método trasfere_para, ele deve armazenar as informações da transação no histórico
- Na conta1 realize: um depósito, um saque, transferência para conta 2 e um extrato, teste.
- Crie a connta2 (objeto) com o respectivo cliente
- Mostre o histórico das duas contas.
- Na conta2 realize: um depósito, um saque, um extrato e a transferência para conta 1.
15- Crie o extrato2 mais completo, mostre também os dados do cliente (nome, sobrenome e cpf)
- Na funcionalidade histórico, acrescente o dia e hora de cada transação.
- Altere o histórico para mostrar também o nome do correntista.             """

from datetime import datetime
import time
class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_sobrenome(self):
        return self.sobrenome
    def get_cpf(self):
        return self.cpf
    def nome_completo(self):
        nc = f'{self.nome} {self.sobrenome}'
        return nc
class Historico:
    def __init__(self):
        self.data_abertura = datetime.today()
        self.transacoes = []
    def get_data_abertura(self):
        return self.data_abertura
    def get_transacoes(self):
        return self.transacoes
    def mostra_historico(self):
        self.transacoes.append("Impressão do histórico em {}".format(datetime.today()))
        print("Histórico:\nAbertura: {}".format(self.data_abertura))
        print("Transações:")
        for t in self.transacoes:
            print("-", t)
    def mostra_historico2(self, nome):
        self.transacoes.append("Impressão do histórico em {}".format(datetime.today()))
        print("Histórico:\nAbertura: {}".format(self.data_abertura))
        print("Histórico do {}:\nAbertura: {}".format(nome, self.data_abertura))
        print("Transações:")
        for t in self.transacoes:
            print("-", t)
class Conta:
    def __init__(self, numero, cliente, saldo, limite=1000.0):
        self.numero = numero
        self.titular = cliente          # Objeto da classe Cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()    # Chama o construtor (__init__) da classe Historico
        ''' Com esse código, toda nova Conta criada já terá um novo Historico associado, 
        sem necessidade de instanciá-lo logo em seguida da criação (instanciação) de uma Conta.'''
    def get_titular_nome(self):
        return self.titular.nome
    def set_titular_nome(self, nome):
        self.titular.nome = nome
    def get_titular_sobrenome(self):
        return self.titular.sobrenome
    def get_titular_cpf(self):
        return self.titular.cpf
    def get_saldo(self):
        return self.saldo
    def get_historico(self):
        return self.historico
    def get_titular(self):
        return self.titular.__dict__  # cliente.__dict__
    def deposito(self, valor):
        self.saldo += valor
        self.historico.get_transacoes().append("Depósito de R${}".format(valor))
    def deposito2(self, valor):
        self.saldo += valor
        dia_hora = datetime.today()
        self.historico.get_transacoes().append("Depósito de R${} em {}".format(valor, dia_hora))
        # self.historico.get_transacoes().append("Depósito de R${} em {}".format(valor, datetime.today()))
    def saque(self, valor):
        if self.saldo + self.limite < valor:
            print('Saldo insuficiente.')
            return False
        else:
            self.saldo -= valor
            print('Saque realizado.')
            self.historico.get_transacoes().append("saque de R${}".format(valor))
            return True
    def extrato(self):
        print("Extrato 1:\nNúmero: {}, Saldo: {}".format(self.numero, self.saldo))
        self.historico.get_transacoes().append("Solicitou o extrato 1.")
    def extrato_2(self):
        print(f'Extrato 2:\nNome: {self.titular.get_nome()} {self.titular.get_sobrenome()}, CPF: {self.titular.get_cpf()}')
        # print(f'Extrato 2:\nNome: {self.titular.nome} {self.titular.sobrenome}, CPF: {self.titular.cpf}')
        print("Número: {}, Saldo: {}".format(self.numero, self.saldo))
        # self.historico.get_transacoes().append("Solicitou extrato 2 em {}".format(datetime.today()))
    def transfere_para(self, destino, valor):
        retirou = self.saque(valor)
        if not retirou:                    # if retirou == False:
            print('Transferência não realizada')
            return False
        else:
            destino.deposito(valor)
            print('Transferência realizada com sucesso')
            self.historico.get_transacoes().append("transferência de R$ {} para conta {}".format(valor, destino.numero))
            return True


if __name__ == '__main__':  # main <tab>
    cliente1 = Cliente('João', 'Oliveira', '11111111111-11')
    conta1 = Conta('123-4', cliente1, 1000.0)       # Chama o construtor de Conta e passa um objeto da classe Cliente
    time.sleep(1)
    conta1.deposito(250)
    time.sleep(1)
    conta1.get_historico().mostra_historico()
    conta1.historico.mostra_historico()
    conta1.deposito(100.0)
    time.sleep(1)
    conta1.saque(50.0)
    time.sleep(1)
    conta1.get_historico().mostra_historico()
    conta1.extrato()
    conta1.get_historico().mostra_historico()
    cliente2 = Cliente('José', 'Azevedo', '222222222-22')
    conta2 = Conta('123-5', cliente2, 1000.0)       # Chama o construtor de Conta e passa um objeto da classe Cliente
    conta1.transfere_para(conta2, 200.0)
    print('conta1.get_saldo()', conta1.get_saldo())
    print('conta2.get_saldo()', conta2.get_saldo())
    conta1.get_historico().mostra_historico()
    conta2.get_historico().mostra_historico()
    conta1.extrato()
    # Extrato: número: 123-4, saldo: 850.0
    conta1.extrato_2()
    print('Abertura: ', conta1.historico.get_data_abertura())
    conta1.get_historico().mostra_historico()
    conta2.extrato()
    conta2.extrato_2()
    conta1.deposito2(222.0)
    conta2.get_historico().mostra_historico()                               # Histórico sem nonme
    nome_cliente = conta2.get_titular_nome()
    conta2.historico.mostra_historico2(nome_cliente)                        # Histórico com nome
    # conta2.historico.mostra_historico2(conta2.get_titular_nome())         # Histórico com nome
    # Lista todos métodos e atributos que a classe possui.
    print('dir(Conta):\n', dir(Conta))
    print('conta1.__class__ :\n', conta1.__class__)
    # Retorna um dicionário com os atributos da classe.
    print('conta1.__dict__ :\n', conta1.__dict__)
    # A função embutida do Python, vars(), chama o __dict__ de uma classe. Retorna um dicionário com os atributos
    print('vars(conta1):\n', vars(conta1))