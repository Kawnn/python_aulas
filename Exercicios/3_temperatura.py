#=================================================================
#Autor: Kawan Kazuo
#Data: 24/05/2024
#Versão: 1.0
#Descrição: Faça um algoritimo que receba a temeperatura em
#           °C e converta para °F e K 
#           
#           --------------------------------------------------
#           Exemplo de execução
#           Insira a  Temperatura em Celsius: 0 
#           Fahrenheit: 32°F
#           Kelvin: 273,15 K
#           --------------------------------------------------
#==================================================================
#variaveis
celsius = 0 #temperatura em Celsius insirida pelo usúario
fahrenheit = 0 #temperatura em Fahrenheit vinda da conversão 
kelvin = 0 #temperatura  em kelvin vinda da conversão 
#entrada
celsius = float(input('Insira a temperatura em Celsius: '))
#processamento
fahrenheit = (celsius * (9/5)) + 32 
kelvin = celsius + 273.15
#saida
print(celsius,'°C equivalem', fahrenheit,'°F' )
print(celsius,'°C equivalem', kelvin,'K')
#==================================================================