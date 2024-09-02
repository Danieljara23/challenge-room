# Contar F's
def contar_f(palabra):
    cantidad_f = palabra.count('F')
    return cantidad_f

palabra = input("Ingresa una palabra: ")
resultado = contar_f(palabra)
print(f"La cantidad de 'F' en la palabra es: {resultado}")


