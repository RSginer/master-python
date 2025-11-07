from mimodulo import suma
from datetime import datetime
from math import sqrt, pi
from random import randint

resultado = suma(5, 7)

print("El resultado de la suma es:", resultado)

print(datetime.now().strftime("%d/%m/%Y"))

print(sqrt(16))
print("El valor de pi es:", pi)

print("Número aleatorio entre 1 y 10:", randint(1, 10))