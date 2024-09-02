def contar_caracteres(word, letter):
    count = 0
    for i in range(len(word)):
        if word[i] == letter:
            count +=1
    return count

print(contar_caracteres("FFFFF", "WWWWWW")) 

