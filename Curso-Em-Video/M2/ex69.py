# -*- coding: utf-8 -*-
print('\n Cadastre uma pessoa')
maior = 0
h = 0
mm20 = 0
while True:
    idade = int(input('Idade:'))
    sexo = str(input('Sexo: [M/F] ')).upper()
    op = str(input('Deseja continuar?[S/N] ')).upper()
    if idade > 18:
        maior +=1
    if sexo == 'M':
        h += 1
    if sexo =='F' and idade < 20:
        mm20+=1
    if op =='N':
        print(f'\n O total de pessoas com mais de 18 anos é {maior}'
              f'\n Ao todo temos {h} homens cadastrados'
              f'\n E temos {mm20} mulheres com menos de 20 anos de idade')
        break
