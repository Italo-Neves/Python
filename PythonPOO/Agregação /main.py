from classes import CarrinhoCompras, Produto
carrinho  = CarrinhoCompras()

p1 = Produto('Camisa',50)
p2 = Produto('iphone',10000)
p13 = Produto('Caneca',20)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.lista_produto()
print(carrinho.soma_total())