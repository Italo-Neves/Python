import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('O site Pudm não está disponivel no momento. ')
else:
    print('Consegui acessar o site pudim com sucesso!')
    print(site.read()) #lê o conteúdo HTML do site