import requests
from bs4 import BeautifulSoup




def trade_spider(limitePag):
    href = ''
    pagina = 1
    jafoi = False
    print('Aguarde......\n\n')
    while pagina <= limitePag:
        url = 'http://solegendas.com.br/series/page/' + str(pagina)
        cod_fonte = requests.get(url)
        textoCod = cod_fonte.text
        sopa = BeautifulSoup(textoCod, "html.parser")
        for link in sopa.findAll('a', {'title': todo}):
            href = link.get('href')
            if href != '':
                jafoi = True
        pagina += 1
        if jafoi:
            break
    print('.:Link para informações: '+href)
    get_single_item_data(href)
    print('\n\nFim')


def get_single_item_data(item_url):
    cod_fonte = requests.get(item_url)
    textoCod = cod_fonte.text
    soup = BeautifulSoup(textoCod, 'html.parser')
    for link in soup.findAll('a', {'title':todo}):
        href = link.get('href')
        print('.:Link para download: '+href)



def pegarNome(nome):
    ofi = nome
    return ofi

def pegarTemp(temporada):
    if temporada < 10:
        aux = 'S0' + str(temporada)
    elif temporada > 10 and temporada < 20:
        aux = 'S' + str(temporada)
    elif temporada == 20:
        aux = 'S20'
    else:
        aux = '10'
    return aux


def pegarEp(ep):
    if ep < 10:
        aux = 'E0' + str(ep)
    elif ep > 10 and ep < 20:
        aux = 'E' + str(ep)
    elif ep == 20:
        aux = 'E20'
    else:
        aux = 'E10'
    return aux

nom = ''
temp = ''
ep = ''
print('Bem vindo ao buscador de legenda!\nEste buscador se limita apenas ao site "So legendas" por hora\n'
      'Quanto mais antiga for a legenda buscado, mais tempo demorará para encontra-la.\n'
      'tome cuidado para não digitar informçaões erradas. ')
nom = pegarNome(input('#~Nome da série: '))
temp = pegarTemp(int(input('#~Temporada desejada: ')))
ep = pegarEp(int(input('#~Episódio desejado: ')))
todo = nom + ' ' + temp + ep
print('Buscando - '+todo)
trade_spider(500)
input('\n\nPressione enter para sair...')





