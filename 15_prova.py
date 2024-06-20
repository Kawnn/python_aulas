'''

Autor: Kawan Kazuo
Data: 13/06/2024
Algoritimo Prova
Descrição: faça um programa que receba dois valores, sendo que o
        primeiro deve ser menor que o segundo.
        O programa deve apresentar todos os numeros impares
        contidos nesta sequencia.
        (Modulo % Exemplo: 7%2 = 1)

'''
valorUm = 0
valorDois = 0
num  = 0

valorUm = int(input('Digite o primeiro valor: '))
valorDois = int(input('Digite o segundo valor maior que o primeiro'))

for num in range(valorUm + 1, valorDois):
    if num % 2 != 0:
        print(num)                                                                                                                                                                     
    