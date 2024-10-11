def contar_vogais_espacos(texto):
    vogais = "aeiouAEIOU"
    contador_vogais = 0
    contador_espacos = 0
    
    for char in texto:
        if char in vogais:
            contador_vogais += 1
        elif char == " ":
            contador_espacos += 1
            
    return contador_vogais, contador_espacos


texto = input("Digite uma string: ")


vogais, espacos = contar_vogais_espacos(texto)


print(f"Número de vogais: {vogais}")
print(f"Número de espaços: {espacos}")
