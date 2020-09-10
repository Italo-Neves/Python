# -*- coding: utf-8 -*-
print('Loja super baratão!')
barato = 9999
pbarato =' '
total = 0
m1k = 0
while True:
    nome = str(input('Digite o nome do produto: ')).upper()
    preco = float(input('Digite o valor do produto: '))
    op = str(input('Deseja continuar? [S/N] ')).upper()
    total += preco
    if preco >1000:
        m1k += 1
    if preco < barato:
        barato = preco
        pbarato = nome
    if op =='N':
        print(f'\n O total da compra foi: R${total}'
              f'\n Temos {m1k} produto que custa mais de R$1000,00'
              f'\n O produto mais barato foi {pbarato} custando {barato}')
        break
