import mod108
p = float(input('Digite o preco: R$'))
print(f'A metade de {mod108.moeda(p)} é {mod108.moeda(mod108.metade(p))} ')
print(f'O dobro de {mod108.moeda(p)} é {mod108.moeda(mod108.dobro(p))}')
print(f'Aumentando 10%, temos {mod108.moeda(mod108.aumentar(p,10))}')