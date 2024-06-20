#Autor: Kawan Kazuo
#Data: 07/06/2024
#Versão 1.0
#=========================================================================================
#algoritimo: senha
#descrição: faça um programa que solicite para o usúario a senha de acesso 
#          ao sistema, ele terá no maximo três tentativas para insirir a correta
#          cadastrada(senai115), caso passe desse limite uma mensagem de erro deve aparece.
#            
#===========================================================================================
#variaveis
senha = '' #var para receber a senha do usúario
senhaPadrao = 'senai115'#senha padrao do sistema 
tentativas = 3
while True:
    senha = input('Digite a sua senha')
    #senai115 => numeros com letras estao sem casting 
    if senha == senhaPadrao:
        print('Acesso liberado')
        break #quebra o loop while, ou seja finaliza o programa 
    else:
        tentativas = tentativas - 1 # tentativas -=1
        print('Voce só possui mais', tentativas, 'tentativas')
    if(tentativas <= 0 ):
        print('Sistema bloqueado')
        break

        
    
        


#entrada
#processamento
#saida


