# Inicio de programa 
from math import inf


print("bem vindo ao sistema de gestao de notas de alunos")

# passo um 1: Adicionar notas manualmente
nota1 = float(input("digite a nota do aluno 1: "))
nota2 = float(input("digite a nota do aluno 2: "))
nota3 = float(input("digite a nota do aluno 3: "))
nota4 = float(input("digite a nota do aluno 4: "))
nota5 = float(input("digite a nota do aluno 5: "))

# Armazenar as notas em uma lista
notas = [nota1, nota2, nota3, nota4, nota5]

# passo dois 2: Calcular a média das notas
soma_notas = 0
for nota in notas:
    soma_notas += nota 
    media = soma_notas / len(notas)
else:
    media = 0

# passo 3: determinar a situacao
if media >= 7:
    situacao = "Aprovado"   
else:
    situacao = "Reprovado"  

    #passo 4 exibir relatorio final
    print("\nRelatório Final:")
    print("notas:", notas)
    print("média:", media)
    print("situação:", situacao)
    
    
