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

carro_ranger = Car("Branco")
print(carro_ranger.cor)
print(carro_ranger.numero_eixos)
