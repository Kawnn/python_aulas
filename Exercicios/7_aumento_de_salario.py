#Autor: Kawan Kazuo
#Data: 04/06
#Versão 1.0
#=========================================================================
#algoritimo: Aumento de salario
#descrição: Faça um programa que receba o salario de um funcionario, calcule e mostre o novo salario, sabendo-se que:
#        salario < R$ aumento de 25$
#        salario >= R$ 1000,00 e <= R$ 2000,00 aumento de 15%                 
#        salario >= R$ 2000,00 aumento de 10%                   
#                           
#                           
#                           
#                           
#===========================================================================
#variaveis
salario = 0
salario_aumento = 0
#entrada
salario = float(input('Digite o seu salario: '))
#processamento
if salario < 1000:
    salario_aumento  = salario * 1.25
    print(round(salario_aumento))
elif(salario >= 1000 and salario < 2000):
    salario_aumento  = salario * 1.15
    print(round(salario_aumento))
elif(salario >=2000):
    salario_aumento  = salario * 1.1
    print(round(salario_aumento))
#saida