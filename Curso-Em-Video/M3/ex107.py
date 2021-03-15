import mod107
p = float(input('Digite o preco: R$'))
print(f'A metade de {p} é R${mod107.metade(p)} ')
print(f'O dobro de {p} é R${mod107.dobro(p)}')
print(f'Aumentando 10%, temos R${mod107.aumentar(p,10)}')