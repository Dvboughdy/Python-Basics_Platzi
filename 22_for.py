import random
import os

os.system("clear")


""" recorrer un diccionario con varios diccionarios dentro usando la funcion dict() """
people = dict(
    person1 = dict(
        name = 'David',
        age = 30,
    ),
    person2 = dict(
        name = 'Juan',
        age = 25,
    ),
    person3 = dict(
        name = 'Pedro',
        age = 35,
    )
)
for person in people.values(): # se recorre el diccionario people y se muestra el valor de cada persona
    print(person['name'], person['age']) # se imprime el nombre y la edad de cada persona

for person, value in people.items(): # se recorre el diccionario people y se muestra el valor de cada persona
    print(person, '=>', value['name'], value['age']) # se imprime el nombre y la edad de cada persona