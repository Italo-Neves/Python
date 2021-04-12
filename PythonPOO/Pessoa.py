from random import randint
class Pessoa:
    ano_autal = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_autal - self.idade)


    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_autal - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand

if __name__ == '__main__':

    p1 = Pessoa('Joseph', 23)
    #print(p1.get_ano_nascimento())
    print(Pessoa.gera_id())
