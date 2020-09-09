# -*- coding: utf-8 -*-
print('\n----------Fatorial-----------')
n = int(input('Digite um número: '))
nf=n-1
n1 = n
while nf >0:
    n = n * nf
    nf = nf - 1
print(f'{n1}! é {n}')
