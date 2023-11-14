"""
    Ex067 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo
    usuário. O programa será interrompido quando o número solicitar for negativo.
    Autor - Samuel Santos
    Empresa - samsantos
"""

while True:
    print('-' * 40)
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)

    if num < 0:
        break

    for c in range(1, 11):
        print(f'{num} X {c:2} = {(num * c):3}')

print('Programa encerrado, volte sempre!')
