nombre = "Ruben"

print(type(nombre))

comprobar = isinstance(nombre, str)
print(comprobar)

if not isinstance(nombre, float):
  print("Esa variable no es un numero con decimales")


text = "     texto con espacios     "

print(text.strip())

print(text.find("con"))