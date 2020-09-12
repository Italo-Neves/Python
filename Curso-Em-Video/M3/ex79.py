# -*- coding: utf-8 -*-
vetor = []
while True:
    n = int(input('Digite um numero: '))
    if n not in vetor:
      vetor.append(n)
    else:
      print('valor Duplicado não irei adicionar!!!')
    op = str(input('Deseja continuar? [S/N] ')).upper()
    if op == 'N':
      break
print(f'O vetor gerado foi: {sorted(vetor)}')
