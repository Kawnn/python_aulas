'''

Autor: Kawan Kazuo
Data: 13/06/2024
Algoritimo "Tabuada 1 ao 9"
Descrição: Faça um programa que apresente a Tabuada 1 ao 10;

'''
#===========================================================

for l in range(11): # 0 => 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10
    for c in range(11): # 0 -> 10
        print(f'{l} x {c} = {l * c}')
        
    