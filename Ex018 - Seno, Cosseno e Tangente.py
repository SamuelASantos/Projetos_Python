# Ex018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor de Seno, Cosseno e Tangente desse
# ângulo
# Autor - Samuel Santos

from math import cos, sin, tan, radians

angulo = float(input('Digite o ângulo que você deseja: '))
grau = radians(angulo)

print(f'O ângulo de {angulo:.1f}º tem o SENO de {(sin(grau)):.2f}')
print(f'O ângulo de {angulo:.1f}º tem o COSSENO de {(cos(grau)):.2f}')
print(f'O ângulo de {angulo:.1f}º tem o TANGENTE de {(tan(grau)):.2f}')
