# txt= input("di un palabra: ")

# def contar_f(txt):
#    return (txt.count("F"))

# print= (contar_f(txt))


palabrita= input("palabrita: ")
letra= input("letra que deseas contar en la palabrita: ")

def contar_caracteres (palabrita):
    return palabrita.count(letra)

print(f"el numero de letras es {contar_caracteres(palabrita)}")
