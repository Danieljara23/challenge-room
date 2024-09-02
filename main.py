# def contar_fs(text):
#     count = 0
#     for i in range(len(text)):
#         if text[i] == "F":
#             count +=1
#     return count

# print(contar_fs("FFS"))

def contar_fs(text):
    return text.count("F")

# print(contar_fs("FFS"))

def contar_caracteres(text, letter):
    return text.count(letter)

print(contar_caracteres("FFfffFFfFC", "f"))
print(contar_caracteres("FFfffFFfFC", "C"))
print(contar_caracteres("FFfffFFfFC", "F"))