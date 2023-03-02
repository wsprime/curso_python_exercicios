class Car:
    def __init__(self, cor):
        self.cor = cor
        self.quantidade_rodas = 5
        self.numero_eixos = 2

    def acelerar(self, intensidade):
        print("Acelerando na intensidade: ", intensidade)
    def frear(self):
        print("Freiando...")

carro_ranger = Car("Branco")
print(carro_ranger.numero_eixos)
