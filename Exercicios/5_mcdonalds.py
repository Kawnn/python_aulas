

#=========================================================================
#descrição  : Escreva um algoritimo para exibir o nome do lanche de acordo
#             do numero inserido pelo usúario, seguinte a tebela abaixo;
#                           Nr.     Lanche
#                           1       Big Mac
#                           2       Quarteirão
#                           3       McChiquen
#                           4       Cheddar McMelt
#                           5       McFish
#===========================================================================
#variaveis
lanche = 0
#entrada
print('******************************************************************************************')
print('Nr. Lanche\n 1. Big Mac \n 2. Quarteirão \n 3. McChiquen \n 4. Cheddar McMelt \n 5. McFish')
lanche = int(input('Insira a opção desejada: '))
#processamento
if lanche == 1:
    print('BigMac')
if lanche == 2:
    print('Quarteirão')
if lanche == 3:
    print('McChiquen')
if lanche == 4:
    print('Cheddar McMelt')
if lanche == 5:
    print('Mcfish')
else:
    print('Opção inválida')

#saida
print('O lanche escolhido foi: ')
print('******************************************************************************************')
#============================================================================