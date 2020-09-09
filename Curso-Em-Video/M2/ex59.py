# -*- coding: utf-8 -*-
maior = 0
op = 0
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
while op != 5:
    op = int(input('O que deseja fazer?'
                  '\n[1] -> somar'
                  '\n[2] -> multiplicar'
                  '\n[3] -> maior'
                  '\n[4] -> novos números'
                  '\n[5] -> sair do programa'))
    if op == 1:
        s =n1+n2
        print(f' {n1} + {n2} = {s}')
    elif op == 2:
        m = n1 * n2
        print(f' {n1} X {n2} = {m}')
    elif op == 3:
        if n1> n2:
            maior = n1
            print(f'O Maior número é {maior}')
        else:
            maior = n2
            print(f'O maior número é {maior}')
    elif op== 4:
              print('\n Escolha novos números')
              n1 =int(input('Digite o primeiro numero: '))
              n2 =int(input('Digite o segundo número: '))


