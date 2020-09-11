# -*- coding: utf-8 -*-
n3 = 0
repet = 0
par = 0
num =(int(input('Digite um número: ')),
      int(input('Digite um número: ')),
      int(input('Digite um número: ')),
      int(input('Digite um número: ')))
for p,n in enumerate(num):
    if n % 2 ==0:
        par +=1
    if 3 in num:
        n3 = p
print(f'Você digitou os valores: {num}')
print(f'O valor 9 se repetiun {num.count(9)} vezes')
print(f'O número 3 apareceu na posição {n3}')
print(f'O total de valore pares foram {par}')
