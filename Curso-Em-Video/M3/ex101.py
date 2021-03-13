from datetime import datetime
def voto_calc(idade):
    voto = ''
    if idade >16 and idade <18 or idade > 70:
        voto = 'VOTO NÂO OBRIGATORIO!'
    elif idade < 70 and idade > 18:
        voto = 'VOTO OBRIGATÓRIO!'
    elif idade < 16:
        voto = 'NÂO VOTA!'
    return voto

def calc_idade(nasc):
    now = datetime.now().year
    idade = now - nasc
    return idade
print('~'*30)
ano_nasc = int(input('Digite o seu ano de nascimento: '))
print(f'Com {calc_idade(ano_nasc)} anos de idade: {voto_calc(calc_idade(ano_nasc))}')