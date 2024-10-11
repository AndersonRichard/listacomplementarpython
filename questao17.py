def ultimo_elemento(lista):
    if not lista: 
        return None
    return lista[-1]


lista = [10, 20, 30, 40, 50]
resultado = ultimo_elemento(lista)

if resultado is not None:
    print(f"O último elemento da lista é: {resultado}")
else:
    print("A lista está vazia.")
