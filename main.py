texto=(input("ingresa un texto: "))
letra=input("ingresa una letra a buscar: ")

def contar_fs(texto):
    cantidad=0
    for i in range(len(texto)):
        if texto[i] == "F":
            cantidad +=1
    return cantidad
def contar_carcateres(texto,letra):
    cant2=0
    for i in range(len(texto)):
        if texto[i] == letra:
            cant2 +=1
    return cant2

print("hay",contar_fs(texto),"F mayuscula")     
print(letra,":", contar_carcateres(texto,letra) )   




