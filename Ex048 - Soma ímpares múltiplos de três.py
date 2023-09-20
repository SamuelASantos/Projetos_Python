'''
    Ex048 - Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se
    encontra no intervalo de 1 até 500.
    Autor - Samuel Santos
    Empresa - samsantos
'''
soma = 0
acc = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        acc += 1
print(f'A soma de todos os {acc} valores solicitados é {soma}')
