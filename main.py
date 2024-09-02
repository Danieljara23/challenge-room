# def contar_fs(word):
#     count = 0
#     for i in range(len(word)):
#         if word[i] == "F":
#             count += 1
#     return count

# def contar_fs(word):
#     return word.count("F")        

word = input("palabra: ")
Letter = input("letra: ")


def contar_caracteres(word, Letter):
    count = 0
    for i in range(len(word)):
        if word[i] == Letter:
            count += 1
    return count  

print(contar_caracteres(word))