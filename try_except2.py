try:
    num = input('Digite um número inteiro, por favor: ')
    num = int(num)
    print(f'O número digitado é: {num}')
except:
    print('Você não digitou um número inteiro! Tente novamente!')