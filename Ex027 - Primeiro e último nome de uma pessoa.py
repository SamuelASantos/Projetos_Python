# Ex027 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
# separadamente.
# Autor - Samuel Santos

nome = str(input('Digite seu nome completo: ')).strip()

listaNome = nome.title().split()

print(f'Seu primeiro nome é {listaNome[0]}.\nSeu último nome é {listaNome[len(listaNome)-1]}.')
