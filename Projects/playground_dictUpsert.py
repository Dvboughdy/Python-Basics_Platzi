import random
import os

os.system("clear")

person = {"name": "Nicolas", "lastName": "Molina", "age": 29}

# Escribe tu solución 👇
#  Agregar un nuevo elemento al diccionario con la llave "twitter" y el valor "@nicobytes".
person["twitter"] = "@nicobytes"
# Actualizar el valor del elemento con la llave "name" con el valor "Felipe".
person["name"] = "Felipe"
# Eliminar el elemento con la llave "age".
person.pop("age")
del person["age"]
# Imprimir una lista con las llaves del diccionario.
print(f"las llaves del diccionario son: {list(person.keys())}")
# Imprimir una lista con los valoresdel diccionario.
print(f"los valores del diccionario son: {list(person.values())}")
