'''
Dsecrição : Faça um programa que receba o dia do mês e apresente ele por extenso:
Sem utilizar condicional
'''
numero_mes = 0
meses =['','janeiro', 'fevereiro', 'março', 'abril'
'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

nome_mes = int(input('Digite o numero do mes(0 a 12)'))

nome_mes = meses[numero_mes - 1]

print(f'O mes correspondente ao numero {numero_mes} é {nome_mes}')