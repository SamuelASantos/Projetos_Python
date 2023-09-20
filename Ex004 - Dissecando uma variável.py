# Ex004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações
# possíveis sobre ele.
# Autor - Samuel Santos

a = input('Digite algo: ')

print(f'O tipo primitivo desse valor é {type(a)}')
print(f'Só tem espaços? {a.isspace()}')
print(f'É um número? {a.isnumeric()}')
print(f'É alphanumérico? {a.isalnum()}')
print(f'É alfabético? {a.isalpha()}')
print(f'Foi escrito em minúsculo? {a.islower()}')
print(f'Foi escrito em caixa alta? {a.isupper()}')
print(f'Foi escrito com a primeira letra maiúscula? {a.istitle()}')
