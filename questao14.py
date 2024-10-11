def maior_menor(lista):
    if not lista:  
        return None, None
    
    maior = lista[0]
    menor = lista[0]
    
    for numero in lista:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
            
    return maior, menor


numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5]
maior, menor = maior_menor(numeros)

print(f"Maior elemento: {maior}")
print(f"Menor elemento: {menor}")
