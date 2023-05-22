import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.error.URLError :
    print('O site não está acessível no momento!')
else:
    print('Tudo okay, o site está no AR!')
    print(site.read())
finally:
    print('Obrigado!')
