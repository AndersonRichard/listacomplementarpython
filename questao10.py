numeros = []

for i in range(10):
    try:
        numero = float(input(f"Digite o {i + 1}º número: "))
        numeros.append(numero)
    except ValueError:
        print("Por favor, digite um número válido.")
        i -= 1


soma = sum(numeros)
maior = max(numeros)
menor = min(numeros)


print(f"\nSoma: {soma}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
