# -*- coding: utf-8 -*-
vetor = []
par = []
impar = []
while True:
    n = int(input('Digite um número: '))
    vetor.append(n)
    op = str(input('Deseja continuar? [S/N]')).upper()
    if n % 2 ==0:
        par.append(n)
    else:
        impar.append(n)
    if op == 'N':
        break
print(f'\n O vetor gerado foi:{vetor}'
      f'\n Os números pares foram: {par}'
      f'\n Os números impares foram: {impar}')
