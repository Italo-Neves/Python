class Produto:
    def __init__(self, idt, descricao, preco=0.0, qtd=1):
        self.idt = idt
        self.descricao = descricao
        self.preco = preco
        self.qtd = qtd

    def get_descricao(self):
        return self.descricao
    def get_preco(self):
        pass