#=================================================================
#Autor: Kawan Kazuo
#Data: 24/05/2024
#Versão: 1.0
#Descrição: Faça um algoritimo que um valor na moeda real (r$),
#           a cotação da conversão REAL para dolar, e apresente 
#           a quantidade desse valor em dolar($)
#           --------------------------------------------------
#           Exemplo de execução
#           Insira o valor em real: 5000
#           Insira cotação do dia: 5
#           R$5000,00 equivalem $1000,00
#           --------------------------------------------------
#==================================================================
#variaveis
real = 0 #recebo o valor em reais 
cotacao = 0 #valor da cotação 1 dolar Xreais
dolar = 0 #valor covertido real para dolar
#entrada
#necessario fazer o cating(conversão de tipos de dados)
#float <= string
#5000,00 <= '5000'
real = float(input('Insira o valor em reais (R$): '))
cotacao = float(input('Insira o valor da cotação: '))
#processamento
dolar = real/cotacao
#saida
print('R$', real, 'equivalem', '$', dolar)
print('=====================================')
#===================================================================