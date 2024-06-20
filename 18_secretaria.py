'''
Descrição : faça um programa que adicione alunos ao sistema da escola
(array) ou remova um aluno
especifico.
        neste sistema deve estar previsto um menu com tres opções:

sistema SENAI
1 - adicionar aluno:
2 - remover aluno:
3 - apresentar alunos
4 - sair
'''
# Lista inicial vazia para armazenar os alunos
lista_alunos = ['joao', 'kawan', 'Luana', 'Kleiton']
escolha = 0
nome_aluno = 0


# Loop principal do programa
while True:
    print("Sistema SENAI")
    print("1 - Adicionar aluno")
    print("2 - Remover aluno")
    print("3 - Apresentar alunos")
    print("4 - Sair")

    escolha = int(input("Digite o número da opção desejada: "))

    if escolha == '1':#adicionando aluno
        nome_aluno = input("Digite o nome do aluno que deseja adicionar: ")
        lista_alunos.append(nome_aluno)
        print(f"Aluno '{nome_aluno}' adicionado com sucesso!")

    elif escolha == '2': #removendo aluno
        nome_aluno = input("Digite o nome do aluno que deseja remover: ")
        if nome_aluno in lista_alunos:
            lista_alunos.remove(nome_aluno)
            print(f"Aluno '{nome_aluno}' removido com sucesso!")
        else:
            print(f"Aluno '{nome_aluno}' não encontrado na lista.")

    elif escolha == '3':#apresentar aluno
        print("\nLista de Alunos:")
        if lista_alunos:
            for index, aluno in enumerate(lista_alunos, start=1):
                print(f"{index}. {aluno}")
        else:
            print("Nenhum aluno cadastrado.")

    elif escolha == '4': #sair do programa
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Escolha novamente.")




