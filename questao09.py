def tabuada(numero):
    print(f"\nTabuada de {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

try:
    numero = int(input("Digite um número inteiro para ver sua tabuada: "))
    
    tabuada(numero)
except ValueError:
    print("Por favor, digite apenas números inteiros válidos.")
