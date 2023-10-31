"""
    Ex061 - Refaça o EXERCÍCIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
    da progressão usando a estrutura while
    Autor - Samuel Santos
    Empresa - samsantos
"""

print('=' * 30)
print('\t10 TERMOS DE UMA PA')
print('=' * 30)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro_termo + (10 - 1) * razao

aux = primeiro_termo
count = 0
while count < 10:
    if aux == 1:
        print(f'{primeiro_termo}', end=' -> ')
    else:
        print(f'{aux}', end=' -> ')
    aux += razao
    count += 1
print('ACABOU!')