numeros = []


for i in range(10):
    while True:
        try:
            numero = int(input(f"Digite o {i + 1}º número inteiro: "))
            numeros.append(numero)
            break 
        except ValueError:
            print("Por favor, digite um número inteiro válido.")


soma = sum(numeros)
media = soma / len(numeros)


print(f"Soma: {soma}")
print(f"Média: {media:.2f}")
