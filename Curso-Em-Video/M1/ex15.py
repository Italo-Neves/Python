# -*- coding: utf-8 -*-
km = float(input('Digite a Quantidade de Km rodados: '))
dia= int(input('Digite a quantidade de dias pelos quais o carro foi alugado: '))

tkm =km * 0.15
tdia=dia *60.0
total= tkm + tdia

print(f'O total da viagem foi R${total}')
