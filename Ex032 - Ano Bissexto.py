# Ex032 - faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
# Autor - Samuel Santos

from datetime import datetime

ano = int(input('Em que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = datetime.now().year

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f'O ano de {ano} É BISSEXTO.')
        else:
            print(f'O ano de {ano} NÃO É BISSEXTO.')
    else:
        print(f'O ano de {ano} É BISSEXTO.')
else:
    print(f'O ano de {ano} NÃO É BISSEXTO.')
