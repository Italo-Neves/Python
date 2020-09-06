# -*- coding: utf-8 -*-
km = int(input('Digite a distancia da viagem em Km: '))

if km < 200:
    preco = km * 0.50
    print(f'O valor total da viagem de {km}Km é R${preco}')
else:
    preco = km * 0.45
    print(f'O valor total da viagem de {km}Km é R${preco}')
