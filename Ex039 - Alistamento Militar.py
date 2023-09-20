# Ex039 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda
# vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento. Seu programa
# também deverá mostrar o tempo que falta ou que passou do prazo
# Autor - Samuel Santos

from datetime import date

nasc = int(input('Ano de nascimento: '))
idade = date.today().year - nasc
ano_atual = date.today().year
falta = (nasc + 18) - ano_atual
passa = ano_atual - (nasc + 18)

print(f'Quem nasceu em {nasc} tem {idade} anos em {ano_atual}.')
if idade < 18:
    print(f'Ainda faltam {falta} anos para o alistamento.')
    print(f'Seu alistamento será em {ano_atual + falta}.')
elif idade > 18:
    print(f'Você já deveria ter se alistado há {passa} anos.')
    print(f'Seu alistamento foi em {ano_atual - passa}.')
else:
    print('Você tem que se alistar IMEDIATAMENTE!')

