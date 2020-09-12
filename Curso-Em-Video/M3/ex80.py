# -*- coding: utf-8 -*-
vetor = []
for i in range(0,5):
    n = int(input('Digie um valor: '))
    if i == 0:
        vetor.append(n)
    elif n > vetor[len(vetor)-1]:
        vetor.append(n)
    else:
        #varre a lista para encontrar a posição correto do numero
        pos = 0
        while pos < len(vetor):
            if n <= vetor[pos]:
                vetor.insert(pos,n)
                break
            pos +=1
print(f'O vetor gerado foi: {vetor}')
