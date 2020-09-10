# -*- coding: utf-8 -*-
print('-------Banco-------')
valor = int(input('Digite quanto quer sacar: '))
total = valor
cin = 50
totdez = 0
totum = 0
totcin= 0
while True:
    if total >= 50:
       total -= 50
       totcin +=1
    if total >= 10:
       total -= 10
       totdez +=1
    if total >= 1:
       total -=1
       totum +=1
    if total ==0:
       break
print(f'\n O total de cedulas utilizadas foram: '
      f'\n {totcin} de cinquenta reais'
      f'\n {totdez} de dez reais'
      f'\n {totum} de um real')
