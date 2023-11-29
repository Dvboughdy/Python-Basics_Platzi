""" Crear un programa que simule el juego de piedra, papel o tijera. """
# Importar librerias para el programa
import random
import os

os.system("clear")

options = ("piedra", "papel", "tijera")  # Crear una tupla con las opciones del juego


user_option = input("piedra, papel o tijera? ")
user_option = user_option.lower()

""" Si la opción del usuario no se encuentra en la tupla options """
if user_option not in options:
    print("Error, por favor ingresa una opción valida")
    exit()  # Termina el programa
"""  """
computer_option = random.choice(
    options
)  # Selecciona un elemento de la lista al azar a partir de la libreria random


""" Nuevos cambios """
print("user_option =>", user_option)
print("computer_option =>", computer_option)
"""  """

if user_option == computer_option:
    print("Empate")

# Usar piedra
elif user_option == "piedra":
    if computer_option == "tijera":
        print("Ganaste, piedra gana a tijera")
    else:
        print("papel gana a piedra")
        print("La computadora gana")

# usar papel
elif user_option == "papel":
    if computer_option == "piedra":
        print("Ganaste, papel gana a piedra")
    else:
        print("Tijera gana a papel")
        print("La computadora gana")

# usar tijera
elif user_option == "tijera":
    if computer_option == "papel":
        print("tijera gana a papel")
        print("usuario gana")
    else:
        print("piedra gana a tijera")
        print("La computadora gana")
