# -*- coding: utf-8 -*-
from math import pow, sqrt
cat=float(input('Digite o cateto oposto: '))
caa=float(input('Digite o cateto adjacente: '))

hip=sqrt(pow(cat,2)+pow(caa,2))

print(f'O valor da hipotenusa é {hip:.2f}')
