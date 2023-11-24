name = input("Ingresa tu nombre: ")
print(name)
age = input("Ingresa tu edad: ")
print(age)

total = 10
age = int(age)
total += age

template = (
    f"Hola mi nombre es {name}, tengo {age} años y en 10 años tendré {total} años"
)
print(template)
