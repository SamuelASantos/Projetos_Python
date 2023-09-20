# Ex037 - Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
# conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal
# Autor - Samuel Santos

num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
escolha = int(input('Sua opção: '))

if escolha == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif escolha == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif escolha == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Escolha uma opção válida.')
