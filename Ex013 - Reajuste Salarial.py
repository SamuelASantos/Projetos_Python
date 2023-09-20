# Ex013 -
# Autor - Samuel Santos

salario = float(input('Qual é o salário do funcionário? R$ '))

print(f'Um salário que ganhava R$ {salario:.2f}, com 15% de aumento, passa a receber R$ {(salario + (salario * 15 / 100)):.2f}')
