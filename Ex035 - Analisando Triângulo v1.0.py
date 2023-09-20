# Ex035 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar
# um triângulo
# Autor - Samuel Santos

print('-=-' * 10)
print('Analisador de Triângulos')
print('-=-' * 10)

s1 = float(input('Digite o primeiro segmento: '))
s2 = float(input('Digite o segundo segmento: '))
s3 = float(input('Digite o terceiro segmento: '))

print('Os segmentos acima PODEM FORMAR triângulo' if s1 + s2 > s3 and s2 + s3 > s1 and s3 + s1 > s2 else 'Os segmentos acima NÃO PODEM FORMAR triângulo')
