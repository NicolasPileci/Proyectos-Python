import random

def dados_al_azar():
    """Imprime dos numeros de un dado al azar, la suma de ellos y pregunta al usuario si desea seguir jugando."""
    lista = [1, 2, 3, 4, 5, 6]
    num1 = random.choice(lista)
    num2 = random.choice(lista)
    print("Numero 1: ", num1)
    print("Numero 2: ", num2)
    print("Suma: ", num1 + num2)
    
print("¿Desea tirar los datos? (Si) - (No)")
resp = input()
while(resp == "Si" or resp == "si"):
    dados_al_azar()
    print("\n¿Tirar otra vez?")
    resp = input()
print("No hay problema. ¡Adios!")


    
