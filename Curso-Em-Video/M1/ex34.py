# -*- coding: utf-8 -*-
sal = float(input('Digite o valor do seu salário: '))

if sal > 1250:
    nsal = sal + (sal * (10/100))
    print(f'O novo salario é : {nsal}')
else:
    nsal = sal +(sal * (15/100))
    print(f'O novo salário é : {nsal}')
