# -*- coding: utf-8 -*-
c = 0
n = int(input('Digite um número: '))
for i in range(1,n+1):
    if n % i == 0:
        c += 1
if c == 2:
    print(f'O número {n} é primo!')
else:
    print(f'O número {n} não é primo!')
