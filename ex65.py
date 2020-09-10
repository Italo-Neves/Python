# -*- coding: utf-8 -*-
c = 0
s = 0
maior = 0
menor = 99999
op ='S'
while op !='N':
    n = int(input('Digite um número: '))
    c += 1
    s += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    op =str(input('Quer continuar? ')).upper()
    media = s/c
print(f'\n Ao total você digitou: {c} números e a média deles foi: {media}'
      f'\nO maior número foi: {maior} o menor número foi: {menor} ')
