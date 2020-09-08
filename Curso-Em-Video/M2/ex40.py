# -*- coding: utf-8 -*-
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1+n2)/2

if media < 5.0:
    print(f'A média do aluno foi {media} portanto está reprovado!')
elif media >= 5.0 and media < 6.9:
    print(f'A média do aluno foi {media} portanto ele está de recuperação!')
elif media >= 7.0:
    print(f'A media do aluno foi:{media} ele está aprovado! ')
