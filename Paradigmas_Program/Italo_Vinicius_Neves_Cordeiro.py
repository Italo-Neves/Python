"""
Nome: Italo Vinicius Neves Cordeiro
RA: 21908201
"""
class Disciplina:
    def __init__(self, identificador, nome):
        self._identificador = identificador
        self._nome = nome
        self._professor = []

    @property
    def id(self):
        return  self._identificador

    @id.setter
    def id(self, identificador):
        self._identificador = identificador

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def professor(self):
        return self._professor

    @professor.setter
    def professor(self,professor):
        self.professor = professor

    def cadastra_profesor(self,professor):
        self.professor.append(professor)

    def monstra_dados_disciplina(self):
        print(f'\n Id:{self.id}'
              f'\n Nome: {self.nome}'
              f'\n \n '
              f'Lecionada por: ')
        for professor in self._professor:
           professor.mostra_professor()
    def consulta_nome_professor(self):
        nome = str(input('Digite o nome do professor: '))
        for professor in self._professor:
           if professor.nome == nome:
              professor.mostra_professor()
           else:
               print('Professor não cadastrado!')

    def altera_idade_professor(self, nidadde):
        p = str(input('Qual professor você deseja modificar? '))
        self.consulta_nome_professor()
        nidadde = str(input('Insira o novo nome: '))

    def dados_professor_mais_novo(self):
        pass

#==========================================================================================================================================================================================================

class Professor:
    def __init__(self, cpf, nome, idade):
        self._cpf = cpf
        self._nome = nome
        self._idade = idade
        self._disciplina = None

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self,cpf):
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._nome = idade

    def mostra_professor(self):
        print(f'\n Nome: {self.nome}'
              f'\n CPF: {self.cpf}'
              f'\n Idade: {self.idade}')

    def calcula_data_nascimento(self):
        pass

#===========================================================================================================================================================================================================
if __name__ == '__main__':

    p1 = Professor(12334234,'Italo',22)
    d1 = Disciplina(12312,'Historia')
    Professor.disciplina = Disciplina
    d1.cadastra_profesor(p1)
    d1.monstra_dados_disciplina()
    d1.consulta_nome_professor()
