# Ex022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas
# - O nome com todas minúsculas
# - Quantas letras ao todo (sem considerar espaços)
# - Quantas letras tem o primeiro nome
# Autor - Samuel Santos

nome = input('Digite seu nome completo: ')

print('Analisando seu nome...')
print(f'Se nome em maiúsculas é {nome.upper()}')
print(f'Se nome em minúsculas é {nome.lower()}')
print(f'Seu nome ao todo tem {len("".join(nome.split()))}')
pnome = nome.split()
print(f'Seu primeiro nome é {pnome[0]} e ele tem {len(pnome[0])} letras.')
