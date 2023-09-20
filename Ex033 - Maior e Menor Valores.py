# Ex033 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
# Autor - Samuel Santos

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

print(f'O menor valor digitado foi {min(n1, n2, n3)}')
print(f'O maior valor digitado foi {max(n1, n2, n3)}')
