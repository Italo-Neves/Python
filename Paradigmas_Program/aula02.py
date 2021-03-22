"""   CEUB   -   Ciência da Computação   -   Prof. Barbosa
Atalho de teclado: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha

- Valor default
Quando declaramos as variáveis na classe Conta, aprendemos que podemos atribuir um valor padrão
para cada uma delas. Então, atribuo um valor padrão ao limite, por exemplo, 1000.0 reais.

- Agregação
Aumente a classe Conta, adicione os atributos nome, sobrenome e cpf do titular da conta.
Desvantagem:
Ficamos como muitos atributos e uma Conta não tem os atributos nome, sobrenome e cpf,
Mas, esses atributos são de Cliente e não da Conta
Assim, criamos uma nova classe e fazemos uma agregação, ou seja,
agregar um cliente a conta.
Portanto, a classe Conta tem um Cliente.
Os atributos de uma Conta também podem ser referência (objeto) para outra classe.

- Implemente:
1- Crie a classe Cliente com os atributos nome, sobrenome e cpf.
- Crie os métodos gets e sets.
- Crie um objeto da classe Cliente, teste.
- Crie o método nome_completo
5- Em Conta, altere o atributo nome_cliente (string) para cliente, ele vai receber um objeto cliente.
- Crie um objeto da classe Conta usando o objeto cliente criado
- Mostre o endereço do objeto cliente criado
- Mostre o endereço do objeto conta criado
- Mostre o endereço do objeto cliente criado, usando o objeto conta.
10- Mostre o nome, sobrenome e cpf usando o objeto cliente
- Altere o nome do objeto cliente, teste.
- Mostre o nome, sobrenome e cpf usando o objeto conta.
- Altere o nome do objeto cliente usando o objeto conta, teste.
- Consulte o extrato com os dados: número e saldo da conta
15- Consulte o extrato com os dados: nome, sobrenome, cpf, número e saldo da conta
- Mostre todos os dados do atributo titular da classe Conta
- Use o método __class__ no objeto cliente
- Use o método __class__.__name__ no objeto cliente
- Mostre os atributos do objeto cliente com o método __dict__
- Mostre os atributos do objeto cliente com o método vars  """
class Cliente(object):          # class Cliente:
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
class Conta:                    # class Conta(object):
    def __init__(self, numero, cliente, saldo, limite=1000.0):  # O parãmetro cliente recebe um objeto da classe Cliente
        self.numero = numero
        self.titular = cliente  # O atributo self.titular recebe o endereço do objeto cliente1
        self.saldo = saldo
        self.limite = limite
    def get_titular(self):
        return self.titular
    def get_titular_nome(self):             # Consulta nome do cliente
        return self.titular.nome
    def set_titular_nome(self, novo_nome):  # Altera nome
        self.titular.nome = novo_nome
    def get_titular_sobrenome(self):
        return self.titular.sobrenome
    def get_titular_cpf(self):
        return self.titular.cpf
    def get_saldo(self):
        return self.saldo
    def extrato(self):
        print(f"Extrato 1:\nNúmero: {self.numero}, Saldo: {self.saldo}")
        # print("Extrato 1:\nNúmero: {}, Saldo: {}".format(self.numero, self.saldo))
    def extrato_2(self):
        print(f'Extrato 2:\nNome: {self.titular.nome} {self.titular.sobrenome}, CPF: {self.titular.cpf}')
        print("Número: {}, Saldo: {}".format(self.numero, self.saldo))
    def dados_titular(self):
        return self.titular.__dict__
    def deposito(self, valor):
        self.saldo += valor
    def saque(self, valor):
        if self.saldo + self.limite < valor:
            print('Saldo insuficiente.')
            return False
        else:
            self.saldo -= valor
            print('Saque realizado.')
            return True
    def transfere_para(self, destino, valor):
        retirou = self.saque(valor)
        if not retirou:                    # if retirou == False:
            print('Transferência não realizada')
            return False
        else:
            destino.deposito(valor)
            print('Transferência realizada com sucesso')
            return True

if __name__ == '__main__':  # mai <tab>
    cliente1 = Cliente('João', 'Oliveira', '1111111111-1')  # Cria objeto da classe Cliente
    print('Nome:', cliente1.get_nome())
    conta1 = Conta('123-4', cliente1, 1200.0, 1000.0)       # Cria objeto da classe Conta usando o objeto da classe Cliente
    print(cliente1)              # <conta_agregacao.Cliente object at 0x000002B9DBA4AFD0>, o endereço do objeto cliente1
    print(conta1)                # <conta_agregacao.Conta object at 0x000002B9DBA4AF70>
    print(conta1.get_titular())  # <conta_agregacao.Cliente object at 0x000002B9DBA4AFD0>, o endereço do atributo titular da classe Conta
    print('Nome:', cliente1.get_nome())                     # Consulta usando a classe Cliente
    print('Sobrenome:', cliente1.get_sobrenome())
    print('CPF:', cliente1.get_cpf())
    cliente1.set_nome('Ana')                                # Altera o nome usando a classe Cliente
    print('Nome:', cliente1.get_nome())
    print('Nome completo:', cliente1.nome_completo())
    print('Nome:', conta1.get_titular_nome())               # Consulta usando a classe Conta
    print('Sobrenome:', conta1.get_titular_sobrenome())
    print('CPF:', conta1.get_titular_cpf())
    conta1.set_titular_nome('Alice')                        # Altera o nome usando a classe Conta
    print('Nome:', conta1.get_titular_nome())
    conta1.extrato()
    conta1.extrato_2()
    print('conta1.dados_titular():', conta1.dados_titular())
    print(conta1.get_titular())             # Retorna o endereço
    print('special method or dunder:')
    print(cliente1.__class__)
    print(cliente1.__class__.__name__)
    print(cliente1.__dict__)                # Métodos semelhantes
    print(vars(cliente1))