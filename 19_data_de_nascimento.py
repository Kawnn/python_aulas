#variaveis
dia_atual = 0
dia_nascimento = 0
mes_nascimento = 0
mes_atual = 0
ano_atual = 0
ano_nascimento = 0
idade = 0

# # entrada
print("Digite sua data de nascimento:")
dia_nascimento = int(input("Dia em que nasceu: "))
mes_nascimento = int(input("Mês em que nasceu: "))
ano_nascimento = int(input("Ano em que nasceu: "))

print("\nDigite a data atual:")
dia_atual = int(input("Dia atual: "))
mes_atual = int(input("Mês atual: "))
ano_atual = int(input("Ano atual: "))

# processamento
idade = ano_atual - ano_nascimento
if (mes_atual, dia_atual) < (mes_nascimento, dia_nascimento):
    idade -= 1

# saida
print(f"\nSua idade é {idade} anos.")


