import random
import os

os.system("clear")
my_list = [1, -1, 2, -2, 3, -3, 4, -4]
new_list = []

# En este desafío, se te proporcionará una lista de números llamada my_list. Tu tarea es recorrer esta lista y utilizar un ciclo para seleccionar solo los números positivos. Luego, debes agregar estos números a una nueva lista llamada new_list. Al final del ciclo, debes imprimir los valores contenidos en new_list utilizando la función print.
for element in my_list:
    if element > 0:
        new_list.append(element)
print(new_list)
