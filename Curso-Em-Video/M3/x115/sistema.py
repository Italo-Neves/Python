from x115.lib.interface import *
from time import sleep
from x115.lib.arquivo import *

arq ='cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        #opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta ==3:
        cabecalho('Saindo do sistema ... até logo!')
        break
    else:
        print('\033[31mERRO! Diigite uma opção valida!\033[m')
    sleep(2)
