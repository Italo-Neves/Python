# -*- coding: utf-8 -*-
valor = float(input('Digite o valor do produto: '))
op = int(input("""\nEscolha a forma de pagamento:
                  \n [1] -> Á vista no dinheiro 10% de esconto
                  \n [2] -> Á vista no cartão 5% de desconto
                  \n [3] -> Até 2x no cartão o preço normal
                  \n [4] -> 3X ou mais no cartão 20% de juros
                """))
if op == 1:
    nvalor = valor - (valor*(10/100))
    print(f'O Preço original é {valor} com o desconto do pagamento em dinheiro fica {nvalor}')
elif op == 2:
    nvalor = valor - (valor*(5/100))
    print(f'O novo preço com desconto de 5% é {nvalor}')
elif op == 3:
    print(f'O preço do produto permanece {valor}')
elif op == 4:
    nvalor = valor + (valor*(20/100))
    print(f'O novo prço com acrescimo de 20% é {nvalor}')
