#Autor: Kawan Kazuo
#Data: 04/06
#Versão 1.0
#=========================================================================
#algoritimo: tipo de triangulo
#descrição: faça um programa que receba 3 valores e verifique se eles podem representar os lados 
#          em um triângulo;
#           1- Triangulo escaleno: triangulo que possui todos os lados com medidas diferentes.      
#    
#           2- Triangulo isósceles: triangulo que possui todos os lados com medidas iguais.
#          
#           3- Triangulo equilatero: triangulo que possui todos os lados com medidas iguais.
#             
#           lembrando que a soma das medidas de dois lados de um triangulo é sempre maior que a medida do 
#           terceiro lado.    
#                           
#                           
#                           
#===========================================================================
#variaveis
lado1 = 0
lado2 = 0
lado3 = 0
tipo_triangulo = ''
#entrada
lado1 = float(input("Digite o valor do primeiro lado do triângulo: "))
lado2 = float(input("Digite o valor do segundo lado do triângulo: "))
lado3 = float(input("Digite o valor do terceiro lado do triângulo: "))
#processamento
if((lado1 + lado2) > lado3 and
   (lado1 + lado3 ) > lado2  and
   (lado2 + lado3)> lado1 and
    lado1 > 0 and lado2 > 0 and lado3 > 0):
    print('Triangulo existe')
if(lado1 == lado2 and  lado2 == lado3):
    tipo_triangulo = 'equilatero'
elif(lado1  == lado2 or lado1 == lado3 or lado2 == lado3):
    tipo_triangulo = 'isosceles'
elif((lado1 != lado2) and (lado1 != lado3) and (lado2 != lado3)):
    tipo_triangulo = 'escaleno'
#saida
print (tipo_triangulo)
