# Ex017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

import math

co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Informe o comprimento do cateto adjacente: '))

print(f'Com o CATETO OPOSTO {co} e o CATETO ADJACENTE {ca} teremos a HIPOTENUSA {(math.hypot(co, ca)):.2f}')
