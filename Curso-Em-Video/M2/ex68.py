# -*- coding: utf-8 -*-
import random
c = 0
while True:
    pc = random.randint(1,10)
    n = int(input('Diga um valor: '))
    poi = str(input('Deseja par ou impar? [I/P]')).upper()
    soma = pc + n
    if poi == 'I':
       if soma % 2 !=0:
            print(f'O resultado foi:{soma} Você VENCEU!')
            c += 1
            print(f'Total de partidas {c}')
            break
       elif soma % 2 == 0:
            c += 1
            print(f'O resultado foi: {soma} você PERDEU')
    elif poi =='P':
       if soma % 2 == 0:
            c += 1
            print(f'O resultado foi: {soma} Você VENCEU!')
            print(f'Total de partidas {c}')
            break
       elif soma % 2 != 0:
            c += 1
            print(f'O resultado foi: {soma} você PERDEU')
