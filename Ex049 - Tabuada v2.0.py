'''
    Ex049 - Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um
    laço for
    Autor - Samuel Santos
    Empresa - samsantos
'''
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{num} x {c:2} = {(num * c):3}')
print('\n\n')
