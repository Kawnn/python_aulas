'''
Auor: Kawan Kazuo
data:12/06/2024
Algoritimo "Tabuada"
Descrição: Faça um programa que calcule a tabuada de um numero digitado
        pelo usúario;
'''
Tabuada = 0
resultado = 0

Tabuada = int(input('Insira o nuemero da tabuada: '))

for X in range(1, 11):
    resultado = Tabuada * X
    print(f'{Tabuada} x {X}) = {resultado}') #interpolação f(format)
