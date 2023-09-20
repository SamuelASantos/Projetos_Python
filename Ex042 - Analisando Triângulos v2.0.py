'''
    Ex042 - Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado
    Autor - Samuel Santos
'''
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if (abs(b - c) < a < b + c) and (abs(a - c) < b < a + c) and (abs(a - b) < c < a + b):
    if a == b and a == c:
        print('Os segmentos acima PODEM formar um triângulo EQUILÁTERO.')
    elif a != b and a != c and b != c:
        print('Os segmentos acima PODEM formar um triângulo ESCALENO.')
    else:
        print('Os segmentos acima PODEM formar um triângulo ISÓSCELES')

else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')
