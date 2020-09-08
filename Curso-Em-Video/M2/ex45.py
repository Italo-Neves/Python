# -*- coding: utf-8 -*-
import random

mao =int(input("""
               \n Escolha:
               \n [1] -> Pedra
               \n [2] -> Papel
               \n [3] -> Tesoura
               """))
pc =random.randint(1,3)

if pc == 1 and mao == 1:
    print('O computador escolheu pedra e você também temos um EMPATE!')
elif pc == 1 and mao == 2:
    print('O Computador escolheu pedra e você escolheu papel Você VENCEU!')
elif pc == 1 and mao == 3:
    print('O computador escolheu pedra e você escolheu tesoura você PERDEU!')

elif pc == 2 and mao == 2:
    print('O computador escolheu papel e você também temos um EMPATE!')
elif pc == 2 and mao == 1:
    print('O Computador escolheu papel e você escolheu pedra Você PERDEU!')
elif pc == 2 and mao == 3:
    print('O computador escolheu papel e você escolheu tesoura você VENCEU!')

elif pc == 3 and mao == 3:
    print('O computador escolheu tesoura e você também temos um EMPATE!')
elif pc == 3 and mao == 2:
    print('O Computador escolheu tesoura e você escolheu papel Você PERDEU!')
elif pc == 3 and mao == 1:
    print('O computador escolheu tesoura e você escolheu pedra você VENCEU!')




