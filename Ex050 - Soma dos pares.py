'''
    Ex050 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se
    o valor digitado for ímpar, desconsidere-o
    Autor - Samuel Santos
    Empresa - samsantos
'''
soma = 0
for c in range(0, 6):
    n = int(input(f'Digite o {c + 1} valor: '))
    if n % 2 == 0:
        soma += n
print(f'A soma dos números pares informados é de {soma}')
