"""
    Ex065 - Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média
    entre todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou
    não continuar a digitar valores.
    Autor - Samuel Santos
    Empresa - samsantos
"""
cont = 0
maior = 0
menor = 0
quant = 0

while True:
    n = int(input('Digite um número: '))
    if cont == 0:
        maior = n
        menor = n
    quant += n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    cont += 1
    res = input('Quer continuar? [S/N] ')
    if res in ('nN'):
        break

print(f'Você digitou {cont} números e a média foi {quant/cont}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
