# -*- coding: utf-8 -*-
vel = int(input('Qual foi a velocidade registrada? '))
lim = 80
if vel < 80:
    print(f'Ele estava a {vel}Km/h e não ultrapassou o limite.')
else:
    vel2= vel - lim
    multa= vel2 * 7
    print(f'Ele estava a {vel}Km/h a  {vel2}Km/h acima do limite, portanto deve pagar uma multa de R${multa} ')
