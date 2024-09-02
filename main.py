# word = input("Escribe una palabra: ")

# def contar_fs(word):
#     return word.count("F")

# print(contar_fs(word))
    
word = input("Escribe una palabra: ")
letter = input("¿Qué letra quieres verificar?: ")

def contar_caracteres(word, letter):
    return word.count(letter)

print(contar_caracteres(word, letter))

# word = input("Escribe una palabra: ")
# letter = input("¿Qué letra quieres verificar?: ")

# def contar_caracteres(word):
#     count = 0
#     for i in range(len(word)):
#         if word [i] == letter:
#             count += 1
#     return count

# print(contar_caracteres(word))

