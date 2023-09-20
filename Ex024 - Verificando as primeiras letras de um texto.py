# Ex024 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
# Autor - Samuel Santos

city = input('Em que cidade você nasceu? ').strip()

n = city.upper().split()

print(f'{"SANTO" in n[0]}')
