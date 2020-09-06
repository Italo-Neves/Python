# -*- coding: utf-8 -*-
import random
n = random.randint(0,5)
n2=int(input("Tente adivinhar em qual número de 0 a 5 eu estou pensando. "))

if n == n2:
    print(f'Você acertou o número era: {n2}')
else:
    print(f'Você errou o número era: {n}')


