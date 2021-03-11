"""
Dicionarios são variavees compostas formadas por conteúdos referenciados por chaves.
os dicionarios são declarados entre {x:y} onde x é a chave e y é o conteúdo referenciado
"""

pessoa ={'Nome':'Italo','sexo':'Masculino','Idade':'21'}
#print(pessoa)
#print(f'O {pessoa["Nome"]} tem {pessoa["Idade"]} anos de idade') # print formatado
#print(pessoa.keys())# -> mostra as chaves existentes no dicionário
#print(pessoa.values())# -> mostra os valores existentes no dicionário
#print(pessoa.items())# -> mostra tudo que está contido no dicionário

#USANDO LAÇOS DE REPETIÇÃO
"""
for k in pessoa.keys():
    print(k) #mostrará apenas as chaves do dicionário
"""
"""
for v in pessoa.values():
    print(v)# mostra os valores do dicionario
"""

"""
for k, v in pessoa.items():
    print(f'{k} = {v}') #mostra todo o conteudo do dicionario
"""
#del pessoa['sexo'] # deleta a chave sexo do dicionario
#pessoa['Nome'] = 'Leandro' # podemos mudar o valor da conteudo apenas com o sinal de '='
#pessoa['peso'] = 89.5 # podemos adicionar elementos sem a necessidade do append

#LISTAS COM DICIONARIOS
"""
brasil = []
estado1 = {'uf':'Rio de janeiro','sigla':'RJ'}
estado2 = {'uf':'São Paulo','Sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
"""
# para adicionar dicionários em uma lista usando laçõs de repetição, nos devemos fazer uma copia do dicionário após preencher os dados
"""
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['Sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy()) # sem o parametro .copy os primeiro dados inseridos no lacõ de for serão repetido até o final do programa
print(brasil)
"""