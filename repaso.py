"""
4 - Escribir un programa que pida al usuario ingresar su nombre y luego imprima un
saludo personalizado dependiendo de la hora del día.

7 - 12 : Buenos días
13 - 20 : tardes
21 - 06: buenas noches
"""

import datetime
anio = datetime.datetime.now().year

fechaNac = int(input("Ingrese su fecha de nac: "))

edad = anio - fechaNac

if edad < 18:
    print("Es menor de edad")
else:
    print("Es mayor de edad")
