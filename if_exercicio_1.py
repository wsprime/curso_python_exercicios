# Faça um programa em python que receba o nome e a nota de um aluno
# Use a função input() e use a função int().

# Caso a nota seja maior ou igual a 7, imprimir Aprovado
# Caso seja menor, imprimir Recuperação


nome = input("Digite seu nome: ")
nota = input("Digite sua nota: ")
print(f'Seu nome é {nome} e sua nota é {nota}')

nota = int(nota)

if nota >= 7 :
    print("Aprovado!")
else:
    print("Recuperação!")
