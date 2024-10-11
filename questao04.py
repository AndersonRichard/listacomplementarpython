def divisores(numero):
    divs = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divs.append(i)
    return divs

try:
    numero = int(input("Digite um número inteiro positivo: "))
    
    if numero > 0:
        divs = divisores(numero)
        print(f"Os divisores de {numero} são: {divs}")
    else:
        print("Por favor, digite um número inteiro positivo.")
except ValueError:
    print("Por favor, digite apenas números válidos.")
