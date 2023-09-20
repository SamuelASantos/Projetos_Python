# Ex028 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu
# ou perdeu
# Autor - Samuel Santos

from random import randint

cpu = randint(1,5)

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

user = int(input('Em que número pensei? '))

if user == cpu:
    print(f'Parabéns! Eu realmente pensei no número {cpu}.')
else:
    print(f'Desculpe, eu pensei no número {cpu} e não no {user}')
