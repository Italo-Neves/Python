# -*- coding: utf-8 -*-
c = 0
maior = 0
menor = 99999
for i in range(1,6):
    peso = float(input(f'Digite o peso da {c}º Pessoa: '))
    c += 1
    if peso > maior:
        maior = peso
    if peso < menor:
        menor =peso
print(f'O maior peso foi {maior} e o menor peso foi:{menor}')
