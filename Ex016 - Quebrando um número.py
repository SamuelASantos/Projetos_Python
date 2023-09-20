# Ex016 - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# Autor - Samuel Santos

from math import trunc

num = float(input('Digite um número real: '))

print(f'O número {num} tem a parte Inteira {trunc(num)}')
