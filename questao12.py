def intercalar_listas(lista1, lista2):
    lista_intercalada = []
    i, j = 0, 0
    

    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            lista_intercalada.append(lista1[i])
            i += 1
        else:
            lista_intercalada.append(lista2[j])
            j += 1
    

    lista_intercalada.extend(lista1[i:])

    lista_intercalada.extend(lista2[j:])
    
    return lista_intercalada


lista1 = [1, 3, 5, 7]
lista2 = [2, 4, 6, 8]

resultado = intercalar_listas(lista1, lista2)
print("Lista intercalada:", resultado)
