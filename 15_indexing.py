import random
import os

os.system("clear")

text = "Ella sabe Python"

# Indexing significa que los textos tienen un indicador o una posición
# en donde empieza y en donde termina
# Ejemplo: Ella sabe Python
# Ella sabe Python
# 0123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104
print(text[0])
print(text[1])
print(text[2])
# print(text[999])

# Si se quisiera saber cual es el ultimo caracter de dicho texto es saber el tamaño

size = len(text)
print("size", size)
print(text[size - 1])

# Otra forma de saber el ultimo caracter es poner -1


print(text[-1])

# Slicing es obtener una cadena de texto en especifico
# Ejemplo: Ella sabe Python
# Ella sabe Python
print(text[0:5])
print(text[10:16])
print(text[0:10])
# o simplemente poner
print(text[:10])

print(text[5:-1])
print(text[5:])
print(text[:])

# Saltos al final del Slicing
print(text[10:16:1])
print(text[10:16:2])
print(text[::2])
