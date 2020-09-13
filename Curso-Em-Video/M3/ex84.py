# -*- coding: utf-8 -*-
total = list()
peoples = list()
great = 0
lower = 0
while True:
    name = str(input('Digite o nome: '))
    peoples.append(name)
    wheigth = float(input('Digite o peso da pessoa: '))
    peoples.append(wheigth)
    if len(total) == 0:
        great = lower = peoples[1]
    else:
        if peoples[1] > great:
            great = peoples[1]
        if peoples[1] < lower:
            lower = peoples[1]
    total.append(peoples[:])
    peoples.clear()
    option = str(input('Deseja continuar? [S/N] ')).upper()
    if option == 'N':
        break
print(f'\n A lista formada foi: {total}'
      f'\n No total de :{len(total)} pessoas')
print(f'O maior peso foi {great} do ',end='')
for p in total:
    if p[1] == great:
       print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {lower} do ',end='')
for p in total:
    if p[1] == lower:
       print(f'[{p[0]}]', end=' ')

