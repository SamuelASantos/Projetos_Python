'''
    Ex051 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
    termos dessa progressão.
    Autor - Samuel Santos
    Empresa - samsantos
'''
print('=' * 30)
print('\t10 TERMOS DE UMA PA')
print('=' * 30)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro_termo + (10 - 1) * razao


for c in range(primeiro_termo, decimo + razao, razao):
    print(c, end=' -> ')
print('ACABOU!')