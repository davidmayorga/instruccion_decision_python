"""Ejercicio 1:
Programa para verificar si una persona es  mayor de edad"""

print("-----------------------------")
print("-------Mayor de edad---------")
print("-----------------------------")


# input
edad = int(input("Digite la edad: "))

# processing
if edad >= 18:
    print("La persona es MAYOR DE EDAD")
else:
    print("La persona es MENOR DE EDAD")