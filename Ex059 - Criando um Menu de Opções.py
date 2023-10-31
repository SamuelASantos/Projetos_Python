"""
    Ex059 - Crie um programa que leia dois valores e monstre um menu como abaixo. Seu programa deverá realizar a
    operação solicitada em cada caso.

    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    Autor - Samuel Santos
    Empresa - samsantos
"""


choise = 1
while choise != 5:
    n1 = int(input('Informe o primeiro número: '))
    n2 = int(input('Informe um segundo número: '))
    while choise != 5:
        print('=' * 10)
        print('[1] Somar')
        print('[2] Multiplicar')
        print('[3] Maior')
        print('[4] Novos números')
        print('[5] Sair do programa')
        print('=' * 10)
        choise = int(input('O que gostaria de fazer com esses números? '))

        if choise == 1:
            print(f'A soma entre {n1} e {n2} é {n1 + n2}')
        elif choise == 2:
            print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}')
        elif choise == 3:
            print(f'Entre {n1} e {n2} o maior é {max(n1, n2)}')
        elif choise == 4:
            break
        elif choise == 5:
            print('Volte sempre!')
            break
