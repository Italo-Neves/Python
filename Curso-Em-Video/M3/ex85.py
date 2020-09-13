# -*- coding: utf-8 -*-
total = [[],[]]
count = 1
for i in range(1,8):
    value=(int(input(f'Digite o {count} valor: ')))
    count += 1
    if value % 2 == 0:
        total[0].append(value)
    else:
        total[1].append(value)
print(f'\n A lista formada é {total}'
      f'\n A lista dos pares é {total[0]}'
      f'\n A lista dos ímpares é {total[1]}')
