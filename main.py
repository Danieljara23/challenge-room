# def contar_fs(palabra):
#     contar_fs = palabra.count("F")
#     return contar_fs

# palabra = input("ingresa una palabra")
# resultado = contar_fs(palabra)
# print("la cantidad de F en la palabra es:", resultado)

# def contar_caracteres(palabra):
#     contar_caracteres = palabra.count("f")
#     return contar_caracteres

# palabra = input("ingresa una palabra")
# resultado = contar_caracteres(palabra)
# print("la cantidad de 'f' en la palabra es:", resultado)

# def contar_Fs(word):
#     count = 0
#     for i in range(len(word)):


# def contar_caracteres():
#     texto = input("Introduce una palabra o frase: ")
#     caracter = input("Introduce el carácter que deseas contar: ")
#     cantidad = texto.count(caracter)
#     print(f"El carácter '{caracter}' aparece {cantidad} veces en el texto.")

# if __name__ == "__main__":
#     contar_caracteres()

def contar_caracteres(word, letter):
    return word.count(letter)

print(contar_caracteres("wfwofwfjnfnewowkfeok", "w"))