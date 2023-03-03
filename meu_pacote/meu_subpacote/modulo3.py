def imprime_var(variavel):
    print(variavel)

class Car:

    quantidade_rodas = 5
    numero_eixos = 2

    # Construtor da Classe
    def __init__(self, cor):
        self.cor = cor

    def acelerar(self, intensidade):
        print("Acelerando na intensidade: ", intensidade)

    def frear(self):
        print("Freiando...")