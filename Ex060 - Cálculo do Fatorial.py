"""
    Ex060 - faça um programa que leia um número qualquer e mostre o seu fatorial
    Autor - Samuel Santos
    Empresa - samsantos
"""
from math import factorial

n = int(input('digite um número para calcular seu fatorial: '))

print(f'Calculando {n}! = ', end='')
aux = n
while n != 0:
    if n == 1:
        print(f'{n}', end='')
    else:
        print(f'{n} x ', end='')
    n -= 1
print(f' = {factorial(aux)}')
