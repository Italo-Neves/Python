class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.endereco = []

    def insere_enderecos(self, cidade, estado):
        self.endereco.append(Endereco(cidade,estado))

    def lista_enderecos(self):
        for endereco in self.endereco:
            pass
class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
