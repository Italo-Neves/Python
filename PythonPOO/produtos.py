class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self._preco = self._preco - (self._preco * (percentual/ 100))

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,valor):
        self._nome = valor

    # Getter
    @property
    def preco(self):
        return self._preco
    #setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor,str):
            valor =float(valor.replace('R$',''))

        self._preco = valor


p1 = Produto('Camiseta','R$50')
p1.desconto(10)
print(p1.nome,p1.preco)