"""
    Ex063 - Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elemantos de uma
    Sequência de Fibonacci.
    Autor - Samuel Santos
    Empresa - samsantos
"""

primeiro = 0
segundo = 1
proximo = primeiro + segundo
count = 1
n_termos = int(input('Quantos termos você quer mostrar? '))

while True:
    if count > n_termos:
        break
    elif count == 1:
        print(primeiro, end=' -> ')
    elif count == 2:
        print(segundo, end=' -> ')
    else:
        print(proximo, end=' -> ')
        primeiro = segundo
        segundo = proximo
        proximo = primeiro + segundo
    count += 1
print('FIM')
