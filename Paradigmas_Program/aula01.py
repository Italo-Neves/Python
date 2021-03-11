"""
Quando declaramos as variáveis na classe conta, aprendemos que podemos atribuir um valor padrão
para cada uma delas. então

- Crie uma classe conta com os atributos numero, nome_cliente, saldo, limite.
- Crei os métodos gets e sets.
- Crie um objeto da classe conta passando os dados.
- Mostre o endereço do objeto criado.
- Consulte e mostre os dados da conta.
- Altere o nome do objeto cliente, teste.
- Faça um depósitom, teste.
- Faça  um saque, teste.
- Faça uma transferencia teste.
- Use o método __class__ no objeto cliente
- Use o método __class__m __name__ no objeto cliente.
- Mostre os atributos do objeto cliente com método __dict__
- Mostre os atributos do objeto cliente o método vars
"""
class Conta:
    def __init__(self, numero, nom_cliente, saldo, limite=1000.0):
        self.numero = numero
        self.titular = nome_cliente
        self.saldo = saldo
        self.limite = limite

    def get_titular(self):
        return self.titular

    def set_titular(set, nome):
        self.titular = nome

    def get_saldo(self):
        return self.saldo

    def get_numero(self):
        return self.numero

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if self.saldo + self.limite < self.saldo:

