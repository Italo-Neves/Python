"""   CEUB   -   Bacharelado em Ciência da Computação   -   Prof. Barbosa
Teclas de atalho: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha.

- Implemente as classes necessárias para realizar a manutenção de um cliente.
Precisamos trabalhar com as seguintes características de cliente:
Nome, idade e seus endereços, ou seja, cada cliente pode ter mais de um endereço.

- Implemente:
1- Crie a classe Cliente com os atributos nome, idade e endereços
- Crie os métodos gets
- Crie um objeto da classe Cliente, teste
- Crie a classe Endereco com os atributos cidade e estado
5- Crie os métodos gets
- Insira um endereço para o cliente:
  Na classe Cliente, crie o método insere_endereco, ele recebe duas strings e cria o objeto da classe Endereco, teste
- Na classe Cliente, crie o método mostra_enderecos, teste
- Crie mais um cliente e insira dois endereços pra ele, teste
- Na classe Cliente, crie o método insere_endereco2, ele recebe um objeto da classe Endereco, teste
10- Crie o método mostra_enderecos2 para Melhorar o layout do método , antes de mostrar
    todos os endereços, ele deve mostrar também o nome do cliente, teste.
- Chame o método mostra_enderecos antes de inserir os endereços, ou seja, no início do método main.
  Se não tiver endereços cadastrados, mostre a mensagem "Cliente não tem endereço cadastrado".
12- Crie um método para remover um endereço de um cliente, teste.
13- Altere o endereço de um cliente, ele continua no mesmo estado, mas mudou de cidade, teste.
"""


class Cliente:  # class Cliente(object):  # Nome de classe no singular, pois é um modelo
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []         # Nome de lista no plural, pode ter vários conteúdos
    def get_nome(self):
        return self.nome
    def get_idade(self):
        return self.idade
    def insere_endereco(self, cidade, estado):          # Recebe duas strings
        o_endereco = Endereco(cidade, estado)           # Chama o construtor da classe Endereco
        self.enderecos.append(o_endereco)
        # self.enderecos.append(Endereco(cidade, estado))  # Equivalente as duas anteriores
    def mostra_enderecos(self):
        print(f'- Endereços do cliente:')
        for o_endereco in self.enderecos:               # Percorre a lista self.enderecos
            print(o_endereco.get_cidade(), o_endereco.get_estado())
    def insere_endereco2(self, o_endereco):             # Recebe um objeto da classe Endereco
        self.enderecos.append(o_endereco)
    def mostra_enderecos2(self):
        print(f'- Endereços do cliente {self.nome}')
        for o_endereco in self.enderecos:
            print(o_endereco.get_cidade(), o_endereco.get_estado())
    def mostra_enderecos3(self):
        if self.enderecos == []:    # if len(self.enderecos) == 0:  # if not self.enderecos:
            print("Cliente não tem endereço cadastrado")
        else:
            print(f'- Endereços do cliente {self.nome}')
            for o_endereco in self.enderecos:
                print(o_endereco.get_cidade(), o_endereco.get_estado())
    def remove_endereco(self, o_endereco):
        self.enderecos.remove(o_endereco)


class Endereco(object):
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def get_cidade(self):
        return self.cidade

    def get_estado(self):
        return self.estado


if __name__ == '__main__':
    cliente1 = Cliente('Luis', 32)              # Chama o construtor (__init__) da classe Cliente
    print('- Nome:', cliente1.get_nome())
    print('Idade:', cliente1.get_idade())
    cliente1.mostra_enderecos3()
    cliente1.insere_endereco('Belo Horizonte', 'MG')
    print('- Nome:', cliente1.get_nome())
    cliente1.mostra_enderecos()
    cliente2 = Cliente('Maria', 44)
    cliente2.insere_endereco('Salvador', 'BA')
    cliente2.insere_endereco('Rio de Janeiro', 'RJ')    # Chama o método passando duas strings
    print('- Nome:', cliente2.get_nome())
    cliente2.mostra_enderecos()
    endereco = Endereco('Brasília', 'DF')       # Chama o construtor (__init__) da classe Endereco
    cliente2.insere_endereco2(endereco)         # Chama o método passando um objeto
    print('- Nome:', cliente2.get_nome())
    cliente2.mostra_enderecos()
    cliente2.mostra_enderecos2()                # Equivalente as duas linhas anteriores
    # Cria o cliente 3
    cliente3 = Cliente('João', 19)
    cliente3.insere_endereco('São Paulo', 'SP')
    print('- Nome:', cliente3.get_nome())
    cliente3.mostra_enderecos()
    cliente3.mostra_enderecos2()                # Equivalente as duas linhas anteriores
    cliente2.remove_endereco(endereco)