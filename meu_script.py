import meu_pacote.modulo as modulo
import meu_pacote.modulo2 as modulo2
import meu_pacote.meu_subpacote.modulo3 as modulo3

print(modulo.__name__)

print(modulo.mediana(10,20,30,40,50))
print(modulo2.soma(200,300))

modulo3.imprime_var("Teste de pacotes")

carro_fiesta = modulo3.Car("Brown")
carro_fiesta.frear()