# -*- coding: utf-8 -*-


nas = int(input('Digite o ano de seu nascimento: '))
ano = 2020

idade = ano - nas

if idade < 18:
    falta = 18 - idade
    print(f'você tem {idade} anos, ainda faltam {falta} anos para você se alistar')
elif idade > 18:
    passou = idade - 18
    print(f'Você tem {idade} anos, está {passou} anos atrazado para o seu alisamento!')
elif idade == 18:
    print(f'Você tem 18 anos deve se alista esse ano!!!')
