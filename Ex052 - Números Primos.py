'''
    Ex052 -
    Autor - Samuel Santos
    Empresa - samsantos
'''
acc = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        acc += 1
        print(f'[{c}]', end=' ')
    else:
        print(f'{c}', end=' ')

print(f'\nO número {num} foi divisível {acc} vezes')
print('E por isso ele', end=' ')
if acc == 2:
    print('É PRIMO!')
else:
    print('NÃO É PRIMO!')
