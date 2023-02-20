nota = 6
nome = 'Regis' 

# IF ANINHADO
if nota > 7:
    print(" Voce passou! ")
    print(f' Sua nota eh: {nota}, Eh maior 7')

else:
    if nota == 7:
        print(" Voce passou! ")
        print(f' Sua nota eh: {nota}, Eh igual a 7')
    else:
        print(" Voce reprovou! ")
        print(f' Sua nota eh: {nota}, Eh menor que 7')

# IF NORMAL   
if nota > 7:
    print(" Voce passou! ")
    print(f' Sua nota eh: {nota}, Eh maior 7')

elif nota == 7:
    print(" Voce passou! ")
    print(f' Sua nota eh: {nota}, Eh igual a 7')
    
else:
    print(" Voce reprovou! ")
    print(f' Sua nota eh: {nota}, Eh menor que 7')

# IF COM DUAS VARIAVEIS
nota = 5
final = 4
if nota >=7:
    print(" Voce passou! ")
    print(f' Sua nota eh: {nota}, Eh maior 7')

elif nota >= 5 and final >= 5:
    print(" Voce passou na final! ")
    print(f' Sua nota eh: {nota}, E sua nota da final é: {final}')
    
else:
    print(" Voce reprovou! ")
    print(f' Sua nota eh: {nota}, Eh menor que 7')

print(" O programa terminou")
    
