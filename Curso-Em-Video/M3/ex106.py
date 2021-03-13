c = ('\033[m', # 0 sem cores
     '\033[0;30;41m', # vermelho
     '\033[0;30m;42', # verde
     '\033[0;30m;43', # amarelo
     '\033[0;30m;44', # azul
     '\033[0;30m;45', # roxo
     '\033[7;30m;'    # branco
     );
def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    help(com)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)
    print(c[0], end='')



comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função da bblioteca >'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!',1)