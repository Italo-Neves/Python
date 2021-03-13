def fatorial(n, show=0):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado
    :param show: (opcional) mostra ou não a conta
    :return: O valor de um fatorial de um número n
    """
    f = 1
    for i in range(n, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ',end='')
            else:
                print(' = ',end='')
        f*= i
    return f


print(fatorial(6, show=True))
help(fatorial)