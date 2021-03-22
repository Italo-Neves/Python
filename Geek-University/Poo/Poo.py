"""
Programação Orientada a objeto - POO

- POO é um modelo de paradgma de programação que utiliza mapeamento
de objetos do mundo real para modelos computaconais.

- Paradigma de programação é a forma/metodologia utilizada para
pensar/desenvolver sistemas.

Principais elementos da orientação a orientação a objetos.
- Classe -> Modelo do objeto do mundo real sendo representado computacionalmente.
- Atributo -> Características dp objeto.
- Método -> Comportamento do objeto(funções).
- Construtor -> método especial utilizado para criar objeto.
- Objeto -> instancia da classe.
"""

#--------------------------------------------------------------------------------------------------------------------
"""
POO - Classes 

Em POO , classes nada mais são do que modelos dos objetos do mundo real sendo representados 
computacionalmente.

Classes podem conter: 
    - Atributos -> Repesentam as cracteristicas dos objetos, ou seja , pelos atributos podemos representar 
    computacionalmente os estados de um objeto. No caso da lâmpada, possivelmento iriamos querer saber se a
    lâmpada é de 110 ou 220 volts, se ela é branca, amarela, vermelha, ou de iutra cor, qual é a luminosidade 
    dela etc.
    
    - Métodos -> Representam os comportamentos do objeto, ou seja, as ações que este objeto pode realizar no seu
    sistema. No caso da lampada por exemplo, um comportamento comum que muito provavelmento iriamos querer representar 
    no nosso sistema é o de ligar e desliga a mesma.
    
Para definirmos uma classe me python usamos a palavra reservada 'class' 

OBS: classes sao objetos

"""
#------------------------------------------------------------------------------------------------------------------------------------
"""
POO: Atributos
Atributos representam as características de um projeto. Ou seja, pelos atributos 
nós conseguimos representar  computaconalmete os  estados de um onjeto.

Em python, dividios os atributos em 3 grupos:
    - Atributos de instancia;
    - Atributos de classe;
    - Atributos dinamicos;

# Atributos de instancia:
    São atributos declarados dentro do método construtor.
    - Ao criarmos instâncias/Objetos de uma classe , todas as intâncias terão esses atributos. 
    __ -> indica que o atributo é private
    self -> É o objeto que está usando o método
    
# Atributos publicos e privados: 
    - Atributos privados so podem ser acessados na propria classe 
    - Por converção todos atributos são publicos

# Atributos de Classe
    - São atributos declarados diretamente na classe, ou seja, fora do método construtor.
    geralmente já iniciamos um valor, e este valor é compartilhado entre todas as instancias da classe.
    Ou seja, ao invés de cada  instância da classe ter seus próprios valores como é o caso dos atributos de 
    instâncias, como os atributos de classe todas as instâncias terão o mesmo valor para o atributo.   

# Atributos Dinamicos
    - Um atributo de instância que pode ser criado em tempo de execução, mas o atributo dinamico será exclusivo
    da instância que o criou.
    

"""
#----------------------------------------------------------------------------------------------------------------------


#print(help(list)) para consultas

#class Lampada:
#    def __init__(self, voltagem,cor):
#        self.__voltagem = voltagem # esta linha indica que o objeto Lampada no atributo Voltagem vai receber voltagem
#        self.__cor = cor
#        self.__ligada = False
#
#class ContaCorrente:
#    def __init__(self,numero, limite, saldo):
#        self.numero = numero
#        self.limite = limite
#        self.saldo = saldo
#
#class Usuario:
#    def __init__(self,nome, email, senha):
#        self.nome = nome
#        self.email = email
#       self.senha = senha

#class Produto:
#    imposto = 1.05 # Em java atributos de classe são os atributos estaticos
#    cont = 0
#    def __init__(self, nome, descricao, valor):
#        self.id = Produto.cont +1
#        self.nome = nome
#        self.descricao = descricao
#        self.valor = (valor * Produto.imposto)
#        Produto.cont = self.id

#if __name__ == '__main__':
#    p1 = Produto("Playstation 4","video-game",13000)
#    p1.peso = "800g" # <- atributo de instancia!
#    print(p1.__dict__) # <- retorna todos os atributos na forma de um dicionario.
#    # o comando 'del' deleta atributos dinamicamente.

"""
POO - Métodos
-Meétodos(funções) -> representam os comportamentos do objeto. ou seja, as ações que este objeto poder realizar
no seu sitema.

Em python dividimos os métodos em:

# Métodos de instância
    -> O método dunder init __init__ é um método especial chamado de construtor e 
    sua função é construir o objeto a partir da classe.

    OBS: todo método em python que inicia e finaliza com duplo underline é chamdo de dunder (double Underline)
    OBS: os métodos/funções dunder em python são chamdos de métodos mágicos.
    ATENÇÂO: Não é aconselhado usar dunder em seus métodos, pois pode intereferir nas funções internas do python

    OBS: métodos são escritos em letras minusculas e separadas por underline quando compostos.

# Métodos de classe
    -> Decorador => @classmethod
    -> Não estão vinculados a auma instancia de classe 
    -> São conhecidos como métodos estaticos em outras linguagens 
    -> É idela utilizalos quando a função que desejamos criar não utilizar atributos de instancia 
    -> Métodos privados só podem ser utilizados dentro da sua propria classe

# Métodos estaticos
    -> Decorador => @staticmethod
    -> Não recebe nada em seus parametros
"""
class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.ligada = False

class ContaCorrente:

    contador = 1234
    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador +1
        self.__limite = limite
        self.saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:
    contador = 0
    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador +1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""
        return (self.__valor * (100 - porcentagem))/100

from passlib.hash import pbkdf2_sha256 as cryp #criptografia char256

class Usuario:
    contador = 0
    @classmethod # e necessario para criar um método de classe
    def conta_usuarios(cls):# o parametor é a propria classe
        print(f'Temos {cls.contador} usuario(s) no sistema')

    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador+1
        self.__sobrenome = sobrenome
        self.__nome = nome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)# qual string sera incriptada, o ronund mostra quantos embaralhamentos seram feitos salt = parte do texto que será juntada
        Usuario.contador = self.__id
        print(f'Usuario criado: {self.__gera_usuario()}')
    def nome_comleto(self):
        return f'{self.__nome} {self.__sobrenome}'

    #verifica se a senha digitada é igual a senha registrada
    def checa_senha(self,senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False
    def __gera_usuario(self):
        return self.__email.split('@')[0] #quebra a string no ponto desejado e devolve o que estava antes do parametro na posiçãozeroda lista

user = Usuario(f'Felicity','Jones','felicity@gmail.com','12345679')

# MATERIAL DE ESTUDO!
#nome = input('Informe o nome: ')
#sobrnome =input('Informe o sobrenome: ')
#email = input('Informe o email: ')
#senha = input('Informe a senha: ')
#confirma_senha = input('Confirme a senha: ')
#
#if senha == confirma_senha:
#    user = Usuario(nome,sobrnome,email, senha)
#else:
#    print('Senha não confere...')
#    exit(42)

#print('Usuario criado com sucesso!')

#senha = input('Informe a senha para o acesso: ')

#if user.checa_senha(senha):
#    print('Acesso permitido')
#else:
#    print('Acesso Negado!')

#print(f'Senha user criptografada: {user._Usuario__senha}') #Aceso errado!





#p1 = Produto('Playstation','Videogame',2300)

#print(p1.desconto(40))

#print(user1.nome_comleto())

#print(user2.nome_comleto())

#print(Usuario.nome_comleto(user2))