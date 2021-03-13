def ficha(name='<Desconhecido>',ng=0):
    print(f'O jogador {name} fez {ng} gol(s) no campeonato')


n = str(input('Digite o nome do jogador: '))
g = str(input('Digite o número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() =='':
    ficha(ng=g)
else:
    ficha(n,g)