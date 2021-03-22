"""   CEUB   -   Ciência da Computação   -   Prof. Barbosa
Atalho de teclado: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha

- Valor default
Quando declaramos as variáveis na classe Conta, aprendemos que podemos atribuir um valor padrão
para cada uma delas. Então, atribuo um valor padrão ao limite, por exemplo, 1000.0 reais.

Implemente:
1- Crie a classe Conta com os atributos numero, nome_cliente, saldo, limite.
- Crie os métodos gets e sets.
- Crie um objeto da classe Conta passando os dados
- Mostre o endereço do objeto conta criado
5- Consulte e mostre os dados da conta
6- Altere o nome do cliente do objeto Conta, teste.
- Faça um depósito, teste.
8- Faça um saque, teste.
- Faça uma transferência, teste.
10- Consulte um extrato com os dados: nome, número e saldo da conta
- Use o método __class__ no objeto cliente
- Use o método __class__.__name__ no objeto cliente
- Mostre os atributos do objeto cliente com o método __dict__
14- Mostre os atributos do objeto cliente com o método vars           """
class Conta:
    def __init__(self, numero, nome_cliente, saldo, limite=1000.0):
        self.numero = numero
        self.titular = nome_cliente
        self.saldo = saldo
        self.limite = limite
    def get_titular(self):
        return self.titular
    def set_titular(self, nome):
        self.titular = nome
    def get_saldo(self):
        return self.saldo
    def get_numero(self):
        return self.numero
    def deposito(self, valor):
        self.saldo += valor             # self.saldo = self.saldo + valor
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
    def extrato(self):
        # print("Extrato:\nNome: {}, Número: {}, Saldo: {}".format(self.titular, self.numero, self.saldo))
        print(f"Extrato:\nNome: {self.titular}, Número: {self.numero}, Saldo: {self.saldo}")
if __name__ == '__main__':  # mai <tab>
    conta1 = Conta('123-4', 'João', 1200.0, 1000.0)  # Chama o contrutor (__init__)
    print(conta1)
    # <conta_agregacao.Conta object at 0x000002B9DBA4AF70>
    print('Nome:', conta1.get_titular())    # Consulta      nome_objeto.nome_metodo()
    print('Número:', conta1.get_numero())
    conta1.set_titular('Ana')               # Altera o nome do cliente
    print('Nome:', conta1.get_titular())
    conta1.deposito(200)
    print('Saldo:', conta1.get_saldo())
    conta1.saque(100)
    print('Saldo:', conta1.get_saldo())
    conta2 = Conta('923-4', 'Ailton', 2000.0, 1000.0)  # Chama o contrutor (__init__)
    print(conta1)
    conta1.transfere_para(conta2, 200)      # Transferência da conta1 para a conta2
    conta1.transfere_para(conta2, 4000)     # Transferência da conta1 para a conta2
    conta1.extrato()
    conta2.extrato()
    print('Método especiais:')
    print(conta1.__class__)             # <class '__nain__.Conta'>
    print(conta1.__class__.__name__)    # Conta
    print(conta1.__dict__)              # {'numero': '123-4', 'titular': 'Ana', 'saldo': 1100.0, 'limite': 1000.0}
    print(vars(conta1))                 # {'numero': '123-4', 'titular': 'Ana', 'saldo': 1100.0, 'limite': 1000.0}