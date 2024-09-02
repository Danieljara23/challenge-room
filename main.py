letter=input("Que letra quieres contar")
word=input("Cuantas veces esta esa letra en......")

def contar_caracteres(word, letter):
    return word.count(letter)

print(contar_caracteres(word, letter))