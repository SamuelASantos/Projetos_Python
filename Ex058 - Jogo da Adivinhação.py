'''
    Ex058 - Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só qu agora o
    jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
    Autor - Samuel Santos
    Empresa - samsantos
'''

from random import randint

pc = randint(1, 10)

count = 0
while True:
    user = int(input('Qual o número de 1 a 10 eu pensei? '))
    if user == pc:
        print(f'Parabéns, eu realmente pensei no número {pc}.')
        count += 1
        break
    else:
        print(f'Não, você errou. Tente outra vez.')
    count += 1

print(f'Você acertou na {count}ª tentativa.')