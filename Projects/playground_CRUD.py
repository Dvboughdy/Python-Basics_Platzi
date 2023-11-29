import random
import os

os.system("clear")
letters = ['A', 'B', 'C', 'D', 'E', 'F']

# Escribe tu solución aquí
# Agregar la letra G al final de la lista
letters.append('G')
print(letters)

# Reemplazar la letra en la posición 0 con la letra Z
letters[0] = 'Z'
print(letters)

# Eliminar la letra en la posición C
letters.pop(2)
print(letters)

# Imprimir la lista resultante al revés
letters.reverse()
print(letters)

""" Codigo resultante """
letters.append('G')
letters[0] = 'Z'
letters.pop(2)
letters.reverse()
print(letters)