def notas(*n, sit=''):
    """
    -> Função para analisar notas e situações de varios alunos.
    :param n: uma ou mais notas dos alunos
    :param sit: valor opcional, indicando se deve ou não aceitar a validação
    :return: dicionario com varias informções sobre a situação da turma.
    """
    menor =99999
    maior = 0
    tot = 0
    aluno = dict()
    situacao = ''
    for i in n:
        tot+= i
        med = tot/len(n)
        if  i > maior:
            maior = i
        if i < menor:
            menor = i
        if med <= 7:
            situacao ='BOA'
        if med > 5 and med < 7:
            situacao ='Rasoavel'
        if med < 6:
            situacao ='Ruim'
        aluno['total'] = len(n)
        aluno['maior'] = maior
        aluno['menor'] = menor
        aluno['media'] = med
        if sit:
            aluno['Situacao'] = situacao
    return aluno

resp = notas(5.5,2.5,10, 6.5, sit=True)
print(resp)