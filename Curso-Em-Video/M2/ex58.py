# -*- coding: utf-8 -*-
import random
c = 0
n = int(input('Digite um número: '))
pc = random.randint(0,10)
while n != pc:
    print(f'O Numero que eu pensei era {pc} e você disse {n} infelizmente você errou!!')
    pc = random.randint(0,10)
    n = int(input('Tente novamente, digite um número: '))
    if n == pc:
        print(f'O Numero que eu pensei era {pc} e você disse {n} Parabéns você acertou!!')
