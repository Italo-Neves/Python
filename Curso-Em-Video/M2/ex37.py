# -*- coding: utf-8 -*-
n = int(input('Digite um valor para ser convertido: '))
op= int(input("""Escoolha uma opção para converter a base:
        \n [1] - Binarios
        \n [2] - Octal
        \n [3] - Hexadecimal
        """))
if op == 1:
    print('O número {} em binario é {}'.format(n,bin(n)))
elif op == 2:
    print('O número {} em octal é {}'.format(n,oct(n)))
elif op ==3:
    print('O número {} em hexadecimal é {}'.format(n,hex(n)))
else:
    print('Opção invalida, por favor tente novamente.')
