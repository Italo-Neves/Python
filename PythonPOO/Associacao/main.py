from Escritor import Escritor
from Escritor import Caneta
from Escritor import MaquinaDeEscrever

escritor = Escritor('Joseph')
caneta = Caneta('Bic')
Maquina = MaquinaDeEscrever()

escritor.ferramenta = caneta #associação
escritor.ferramenta.escrever()