# -*- coding: utf-8 -*-
from random import randint
from time import sleep
lis = list()
cont = 0
games = []
amg = int(input('Quantos jogos você deseja fazer?'))
tot = 0
while tot <= amg:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lis:
            lis.append(num)
            cont +=1
        if cont>=6:
            break
    lis.sort()
    games.append(lis[:])
    lis.clear()
    tot +=1
print(f'Os números sorteados foram: {lis}')
for i, l in enumerate(games):
    print(f'games {i}:{l}')
    sleep(1)

