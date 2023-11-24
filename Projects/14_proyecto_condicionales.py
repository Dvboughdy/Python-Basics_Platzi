import random
import os

os.system("clear")

user_option = input("piedra, papel o tijera? ")
user_option = user_option.lower()
computer_option = random.choice(["piedra", "papel", "tijera"])

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
