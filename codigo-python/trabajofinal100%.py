base = input("Ingresa una palabra base: ")

#contar lso caracteres
contador = len(base)

contrasena = ""
indice = 0

#repetir la palabra hasta tener al menos 12 caracteres
"""Si el usuario ingresa 12 caracteres el programa saltara esta parte, pero si no asegurara generar los 12 caracteres"""
while indice < 12:
    for i in range(contador):
        if indice < 12:
            contrasena = contrasena + base[i]
            indice = indice + 1

#contadores de seguridad 
"""Los contadores nos van a funcionar para hacer mayusculas, numeros y simbolos y agregarlos a la palabra inicial"""
mayuscula = 0
numero = 0
simbolo = 0

final = ""

#mejorar la contraseña
"""Entonces la contraseña tendra 12 caracteres obligatoriamente"""
for i in range(12):
    c = contrasena[i]

    if c == "a":
        final = final + "@"
        simbolo = simbolo + 1
    elif c == "e":
        final = final + "3"
        numero = numero + 1
    elif c == "o":
        final = final + "0"
        numero = numero + 1
    elif c >= "a" and c <= "z":
        final = final + c.upper()
        mayuscula = mayuscula + 1
    elif c >= "A" and c <= "Z":
        final = final + c
        mayuscula = mayuscula + 1
    elif c >= "0" and c <= "9":
        final = final + c
        numero = numero + 1
    else:
        final = final + c
        simbolo = simbolo + 1

#asegurar al menos un símbolo
"""la importancia para que una contraseña sea mas segura es tener distintos caracteres siendo simbolos o numeros muy importantes"""
if simbolo == 0:
    final = "!" + final

#asegurar al menos un número 
"""aquí aseguramos"""
if numero == 0:
    final = final + "5"

print("Contraseña mejorada:")
print(final)