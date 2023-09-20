'''
    Ex054 - Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quatas pessoas ainda não
    atingiram a maioridade e quantas já são maiores.
    Autor - Samuel Santos
    Empresa - samsantos
'''
from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = date.today().year - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print(f'Ao todo tivemos {maior} pessoas maiores de idade.')
print(f'E também tivemos {menor} pessoas menores de idade.')
