# -*- coding: utf-8 -*-
tidade = 0
media = 0
maioridadehomem = 0
nomevelho = 0
totmulher20 = 0
for p in range(1,5):
    nome = str(input('Digite o seu nome: '))
    idade =int(input('Digite a sua idade: '))
    sexo = str(input('\n Qual é o seu sexo?'
                     '\n [M] => Masculino'
                     '\n [F] => Feminino')).strip()
    tidade += idade
    if p== 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        totmulher20 += 1
media = tidade/4
print(f'A média de idade do grupo é de {media} anos')
print(f'O homem mais velho tem {maioridadehomem} e se chama{nomevelho}')
print(f'Ao todo são {totmulher20} com 20 anos')
