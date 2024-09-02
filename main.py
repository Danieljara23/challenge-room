# Contar F's
def contar_f(palabra):
    cantidad_f = palabra.count('F')
    return cantidad_f

palabra = input("Ingresa una palabra: ")
resultado = contar_f(palabra)
print(f"La cantidad de 'F' en la palabra es: {resultado}")


# Contar caracteres
def contar_caracteres(palabra, letra):
    cantidad_letra = palabra.count(letra)
    return cantidad_letra

palabra2 = input("Ingresa una palabra: ")
Letra2 = input("Ingresa la letra a detectar: ")
resultado2 = contar_caracteres(palabra2, Letra2)
print(f"La palabra {palabra2} tiene {resultado2} {Letra2}")