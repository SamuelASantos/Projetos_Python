'''
    Ex045 - Jogo JOKENPO!
    Autor - Samuel Santos
'''
from time import sleep
from random import randint

print('Suas opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
jog = int(input('Qual é a sua jogada? '))
com = randint(0, 2)

if jog == com:
    resultado = 'EMPATAMOS'
elif (jog == 0 and com == 1) or (jog == 1 and com == 2) or (jog == 2 and com == 0):
    resultado = 'EU GANHEI! VOCÊ PERDEU!'
elif (jog == 1 and com == 0) or (jog == 2 and com == 1) or (jog == 0 and com == 2):
    resultado = 'EU PERDI =( VOCÊ GANHOU. PARABÉNS!'
else:
    print('Você escolheu uma opção inválida. Tente novamente.')
    exit()

if jog == 0:
    jog = 'PEDRA'
elif jog == 1:
    jog = 'PAPEL'
elif jog == 2:
    jog = 'TESOURA'

if com == 0:
    com = 'PEDRA'
elif com == 1:
    com = 'PAPEL'
elif com == 2:
    com = 'TESOURA'

sleep(.5)
print('JO')
sleep(.5)
print('KEN')
sleep(.5)
print('PO!!!')

print(f'Eu escolhi {com} e você escolheu {jog}.')
print(resultado)
