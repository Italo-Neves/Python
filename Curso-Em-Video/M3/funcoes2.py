"""
help() -> entrar no console de adjuda interativa do python, depois é so digitar em que queremos ajuda
ou então passar como parametro o que queremos pesquisar

print(x.__doc__) -> irá nos fornecer a documentação da função X

Docstrings são a documentão de uma função, elas devem ser criadas abaixo da função criada usando ''' doc '''
"""
# Parametros opcionais:
def somar(a=0,b=0,c=0):#quando queremos que um parametro seja opcional colo
    s = a+b+c # lembre-se que variaveis criads dentro da função só funcionam na função chamadas variaveis locais
    return s #return é útil quando temos queremos apenas o valor resultante

somar(3,2)
# Se quisermos usar uma variavel global em uma função nos colocamos o parametro "global" antes