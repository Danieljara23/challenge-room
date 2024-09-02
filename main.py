text = input("Ingresa una palabra: ")

def contar_fs(text):
    count = 0
    for i in range(len(text)):
        if text [i] == "f": 
            count +=1    
    return count

letter = input("¿Qué letra quieres verificar? ")

def contar_caracteres(text,letter):
    count = 0
    for i in range(len(text)):
        if text [i] == letter:
            count +=1
    return count

print("En la palabra hay", (contar_fs (text)),"f's y ", (contar_caracteres(text,letter)), letter)

# def contar_caracteres(text):
#     count = 0
#     for i in range(len(text)):
#         count +=1
#     return count

# print("En la palabra hay", (contar_fs (text)),"f's y ", (contar_caracteres(text)), "caracteres")