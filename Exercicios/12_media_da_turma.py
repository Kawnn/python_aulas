#Autor: Kawan Kazuo
#Data: 04/06
#Versão 1.0
#=========================================================================
#algoritimo: media turma
#descrição: faça um progarama que receba duas notas de seis alunos. 
#          Calcule e mostre:
#           a mensagem arimetica das duas notas de cada aluno; e
#           a mensagem que esta na tabela a seguir;
#               media arimetica         mensagem
#               ate 3                   Reprovado
#               entre 4 e 7             exame
#               de 8 pra cima           Aprovado
#             
#          O total de alunos aprovados;
#          O total de alunos de exame;
#          O total de alunos reprovados;                
#          A media da classe.                
#                           
#=========================================================================
aluno = 0 
qtdAlunos = 6
alunosAprovado =0
alunosReprovados = 0
alunosExame = 0
somaMedia = 0

while aluno < qtdAlunos:
    aluno = aluno + 1
    #aluno x
    notaUm = 0 
    notaDois = 0
    media = 0
    notaUm = float(input(f'Insira a nota 1 do aluno (aluno):'))
    notaDois = float(input(f'Insira a nota 2 doaluno (aluno):'))

    media = (notaUm + notaDois) /2 #10 -> 8 -> 5 -> 10 -> 7 -> 8
    somaMedia = somaMedia + media #10 -> 18 -> 23 -> 33 ->  =>40 ->40

    if(media <= 3):
        print('Reprovado')
        alunosReprovados += 1 
    elif(media >= 4 and media <= 7):
        print('Exame')
        alunosExame +=1
    else:
        print('Aprovado')
        alunosAprovado +=1

mediaFinal = round((somaMedia / qtdAlunos),2)
print(f'Media final da turma: {somaMedia}')
print(f'Quantidades de alunos aprovado: {alunosAprovado}')
print(f'Quantidades de alunos Reprovados: {alunosReprovados}')
print(f'Quantidades de alunos Exame: {alunosExame}')