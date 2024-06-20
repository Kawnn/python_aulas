
#Autor: Kawan Kazuo
#Data: 04/06
#Versão 1.0
#=========================================================================
#algoritimo: multa e velocidade 
#descrição: faça um programa que leia a velociadade maxima permitida em
#           uma avenida e velocidade com que o motorista estava dirigindo nela e
#           calcule a multa que uma pessoa vai receber:
#          
#          velocidade Ultrapassada         Valor da Multa
#             ate 10km/h                    R$ 50,00
#             11 a 30 km/h                  R$ 100,00
#             mais 31 km/h                  R$ 200,00
#               
#                           
#                           
#                           
#===========================================================================
#variaveis
limiteVelocidade = 0
velocidadeMotorista = 0
diferencaVelocidade = 0
valorMulta = ''
#entrada
limiteVelocidade= int(input('Insira o limite de Velocidade da via: '))
velocidadeMotorista = int(input('Insira a Velocidade do motorista: '))
#processamento
diferencaVelocidade = limiteVelocidade - velocidadeMotorista

if(diferencaVelocidade > 0 and diferencaVelocidade <=10):
    valorMulta = 'R$50,00'
elif(diferencaVelocidade >= 11 and diferencaVelocidade <=30):
    valorMulta = 'R$100,oo'
elif(diferencaVelocidade >=31):
    valorMulta = 'R$200,00'
else:
    valorMulta ='R$0,001' 
#saida
print(valorMulta)
