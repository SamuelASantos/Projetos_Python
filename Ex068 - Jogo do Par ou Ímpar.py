"""
    Ex068 - Faça um programa que jogue par ou ímpar com o computador. O jogo será interrompido quando o jogador PERDER,
    mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
    Autor - Samuel Santos
    Empresa - samsantos
"""

from random import randint

print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)

acc = 0
while True:
    pc = randint(0, 10)
    num = int(input('Diga um valor: '))
    choise = input('Par ou ímpar? [P/I] ').strip().upper()
    soma = num + pc
    print('-' * 30)
    print(f'Você jogou {num} e o computador {pc}. Total de {soma}', end=' ')
    if soma % 2 == 0:
        print('DEU PAR')
        res = 'P'
    else:
        print('DEU ÍMPAR')
        res = 'I'
    print('-' * 30)
    if choise == res:
        acc += 1
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-' * 15)
    else:
        print('Você PERDEU!')
        break
print(f'GAME OVER! Você venceu {acc} vezes')
