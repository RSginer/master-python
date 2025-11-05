"""
Listas
"""
peliculas = ["Batman", "Superman", "Wonder Woman"]
canciones = list(("Imagine", "One", "Billie Jean"))
print(peliculas)

peliculas.remove("Superman")
print(type(peliculas))
print(type(canciones))
print(peliculas[0:2])
print(canciones[1:])

canciones.append("Thriller")
print(canciones)

## Recorrer listas

for pelicula in peliculas:
  print(f"{peliculas.index(pelicula) + 1}. Película: {pelicula}")

for cancion in canciones:
  print(f"{canciones.index(cancion) + 1}. Canción: {cancion}")