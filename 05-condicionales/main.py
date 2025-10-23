
color = input("Ingresa un color: ")

if color == "rojo":
    print("El color es rojo")
elif color == "azul":
    print("El color es azul")
else:
    print("El color no es ni rojo ni azul")

"""Operadores de comparación en Python."""
a = 10
b = 5
print(a == b)  # Igualdad
print(a != b)  # Desigualdad
print(a > b)   # Mayor que
print(a < b)   # Menor que
print(a >= b)  # Mayor o igual que
print(a <= b)  # Menor o igual que

nombre = "Ruben"
ciudad = "Barcelona"
continente = "Europa"
edad = 30
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")
    if continente != "Europa":
        print(f"{nombre} no es europeo")
    else:
        print(f"{nombre} es europeo y vive en {ciudad}")
else:
    print(f"{nombre} es menor de edad")

dia = int(input("Ingresa un número del 1 al 7 para el día de la semana: "))
if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miércoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sábado")
elif dia == 7:
    print("Domingo")
else:
    print("Día inválido")


edad_minima = 17
edad_maxima = 65
edad_usuario = int(input("Ingresa tu edad: "))

if edad_usuario >= edad_minima and edad_usuario <= edad_maxima:
    print("Puedes trabajar")
else:
    print("No puedes trabajar")

pais = input("Ingresa el país donde vives: ")

if not (pais == "Mexico" or pais == "España" or pais == "Colombia") or pais == "Argentina":
    print(f"{pais} es un país de habla hispana.")