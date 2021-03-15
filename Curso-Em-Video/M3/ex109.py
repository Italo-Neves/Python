import mod109
p = float(input('Digite o preco: R$'))
print(f'A metade de {mod109.moeda(p)} é {mod109.metade(p, True)}')
print(f'O dobro de {mod109.moeda(p)} é {mod109.dobro(p, True)}')
print(f'Aumentanexdo 10%, temos {mod109.aumentar(p,10, True)}')