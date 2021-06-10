# -*- coding: utf-8 -*-
while True:
    n =int(input('Quer ver a tabuada de qual número?'))
    if n == 0:
        print('O programa ENCERROU!')
        break
    else:
        for i in range(0,11):
            m = i * n
            print(f'{i} X {n} = {m}')

