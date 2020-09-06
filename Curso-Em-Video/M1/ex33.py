# -*- coding: utf-8 -*-
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

maior = 0
menor =99999

if (n1 > n2) and (n1 > n3):
    maior = n1
    print(f'O maior número é {maior}')
if(n2 > n1) and(n2> n3):
    maior = n2
    print(f'O maior número é {maior}')
if (n3 > n2)and(n3 >n1):
    maior = n3
    print(f'O maior número é {maior}')

