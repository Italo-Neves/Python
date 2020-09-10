# -*- coding: utf-8 -*-
while True:
    n =int(input('Quer ver a tabuada de qual número?'))
    for i in range(0,11):
        m = i * n
        print(f'{i} X {n} = {m}')
    if n == 0:
        break
        print('Programa ENCERRO!')
