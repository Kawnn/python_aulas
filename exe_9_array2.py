'''
Autor: Kawan Kazuo
Data: 17/06/2024
Versão: 1.0
Descrição: Estudo do tipo de dado Array(Vetor)
'''
carros = ['VW']

carros.append('GM')#adiciona na ultima posição o valor idicado
carros.append('Ford')
carros.append('Fiat')
carros.append('renault')
print(carros)

carros.remove('Ford')
print(carros)

carros.pop(3)
print(carros)

carros.pop(3)
print(carros)

print(len(carros))
carros.pop(len(carros) -1)
print(carros)