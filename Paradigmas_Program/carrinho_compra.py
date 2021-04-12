from datetime import datetime
class CarrinhoCompra:
    def __init__(self, num_pedido,o_cliente):
        self.num_pedido = num_pedido
        self.cliente = o_cliente
        self.produtos = list()

    def get_num_pedido(self):
        return self.num_pedido

    def get_cliente_nome(self):
        return self.cliente.get_nome()

    def mostra_carrinho(self):
        print('- Mostra carrinho: ')
        for produto in self.produtos:
            print('Descrição: ',produto.get_descricao)
