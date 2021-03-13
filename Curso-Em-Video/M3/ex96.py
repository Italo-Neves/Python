def controle(x,y):
    c = x * y
    print(f'A área de um terreno {x:.1f}X{y:.1f} é {c:.1f}m²')

print('Controle de Terrenos')
print('-'*30)
lar = float(input('LARGURA (m): '))
con = float(input('COMPRIMENTO (m): '))
controle(lar,con)
