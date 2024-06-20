#=================================================================
#Autor: Kawan Kazuo
#Data: 24/05/2024
#Versão: 1.0
#Descrição: Faça um algoritimo que receba o raio em metros
#           de um circuloe apresente a sua area
#           
#           --------------------------------------------------
#           Exemplo de execução
#           Insira o raio em metros: 
#           Área do circulo: 78.5m2
#           --------------------------------------------------
#
#           a = área 
#           pi = 3.14
#           r = raio
#           a = pi*(r2)
#==================================================================
#variavel
r = 0 #raio
a = 0 #area
pi = 3.14 #constante pi
#entrada
r = float(input('Insira o raio do circulo em metros'))
#processamento
a = pi*(r**2)
#saida
print('A área do circulo é', a , 'm2')
#==================================================================