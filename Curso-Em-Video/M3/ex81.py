# -*- coding: utf-8 -*-
vetor = []
c = 0
while True:
    n = int(input('Digite um número: '))
    vetor.append(n)
    c += 1
    op = str(input('Deseja continuar? [S/N]')).upper()
    if op =='N':
        break
print(f'\n Você digitou {c} elementos'
      f'\n A ordem decrescente do vetor formado é {sorted(vetor,key=int,reverse=True)}')
if 5 in vetor:
    print(f'\n O valor 5 faz parte do vetor!')
else:
    print('\n O valor 5 não faz parte do vetor!')
