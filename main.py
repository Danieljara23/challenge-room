


def contar_caracteres (numerof,caracteres):
   
    count=0
    for i in range (len(numerof)):
        if numerof[i]==caracteres:
            count+=1
    return count

caracteres=input("pon un caracter para ser contado :")
numerof=input("pon una nombre: ")

print(contar_caracteres(numerof,caracteres))

       
       