"""
Ejercicio 4.
Pedir dos numeros al usuario y hacer todas las operaciones básicas de una calculadora
"""

import math


numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2 if numero2 != 0 else "Error: División por cero no permitida"
redondeo = math.ceil(numero1)
print(f"Resultados:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
print(f"Redondeo: {redondeo}")
print("---END CALCULADORA---")