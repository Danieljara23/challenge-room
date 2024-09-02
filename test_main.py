# Contar caracteres
def contar_caracteres(palabra, letra):
    cantidad_letra = palabra.count(letra)
    return cantidad_letra

palabra2 = input("Ingresa una palabra: ")
Letra2 = input("Ingresa la letra a detectar: ")
resultado2 = contar_caracteres(palabra2, Letra2)
print(f"La palabra {palabra2} tiene {resultado2} {Letra2}")
