"""
    Ex062 - Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa
    encerra quando ele disser que quer mostrar 0 termos.
    Autor - Samuel Santos
    Empresa - samsantos
"""

print('=' * 30)
print('\tTERMOS DE UMA PA')
print('=' * 30)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
aux = 0
count = 0

while count < 10:
    if count == 0:
        print(primeiro_termo, end=' -> ')
    else:
        print(primeiro_termo + aux, end=' -> ')
    count += 1
    aux += razao
print('PAUSA')

termos = 10

while True:
    termo = int(input('Quanto termos você quer mostrar a mais? '))
    termos += termo
    count = 0
    if termo == 0:
        break
    while count < termo:
        print(aux, end=' -> ')
        aux += razao - primeiro_termo
        count += 1
    print('PAUSA')
print(f'Progressão finalizada com {termos} termos mostrados.')
