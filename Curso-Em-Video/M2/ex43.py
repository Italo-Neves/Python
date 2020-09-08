# -*- coding: utf-8 -*-
from math import pow
altu = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))
imc =(peso/pow(altu,2))

print(f'seu IMC é {imc:.2f}')

if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc > 18.5 and imc<26:
    print('Você está no peso ideal!')
elif imc > 25 and imc < 31:
    print('Você está com sobre peso!')
elif imc > 30 and imc < 41:
    print('Você está com obesidade!')
elif imc > 40:
    print('Você está com obes morbida!!!')
