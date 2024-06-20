#Autor: Kawan Kazuo
#Data: 04/06
#Versão 1.0
#=========================================================================
#algoritimo: classificação de idade 
#descrição: faça um programa que leia uma idade de um individuo
#           e escreva a faixa etaria e que pertence, de acordo com a tabela abaixo 
#               faixa etaria        classificação
#                <12                criança       
#                13 - 17            adolescente
#                18 - 59            adulto         
#                           
#                           
#                           
#===========================================================================
#variaveis
idade = 0
classificacao = ''
#entrada
idade =int(input('Insira a sua idade'))
#processamento
if(idade >= 0 and idade <12):
    classificacao = 'Crianca'
elif(idade >=13 and idade <= 17):
    classificacao = 'adolescente'
elif(idade >=18 and idade <= 59):
    classificacao = 'adulto'
elif(idade > 59):
    classificacao = 'adulto plus'
else: 
    classificacao = 'idade inserida invalida'
#saida
print(classificacao)