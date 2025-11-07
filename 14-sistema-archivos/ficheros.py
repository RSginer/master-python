from io import open
import pathlib


ruta = pathlib.Path('13-paquetes/main.py')

archivo = open(ruta, "w", encoding="utf-8")
archivo.write("variableNueva = 'Ruben'\n")
archivo.write(f"print(variableNueva)")

archivo.close()

exec(compile(open(ruta, "r", encoding="utf-8").read(), ruta, 'exec'))