def aumentar(preco =0, taxa=0, formato=False):
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preco = 0 , taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preco =0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco =0, formato=False):
    res = preco/ 2
    return res if formato is False else moeda(res)

def moeda(preco =0, moeda ='R$', format=False):
    return f'{moeda}{preco:.2f}'.replace('.',',')

def resumo(preco, au, red):
    print('-' * 40)
    print('RESUMO DO VALOR'.center(40))
    print('-'*40)
    print(f'A Preço analiisado:\t\t{preco}')
    print(f'Dobro do Preço:\t\t\t{dobro(preco, True)}')
    print(f'Metade do preço:\t\t{metade(preco)}')
    print(f'{au}% de Aumento:\t\t\t{aumentar(preco, au, True)}')
    print(f'{red}% de Redução:\t\t\t{diminuir(preco, red, True)}')
    print('-' * 40)