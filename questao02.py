def somar_digitos(numero):
    return sum(int(digito) for digito in str(numero))


try:
    numero = int(input("Digite um número menor que 100: "))
    
    if 0 <= numero < 100:
        resultado = somar_digitos(numero)
        print(f"A soma dos dígitos de {numero} é: {resultado}")
    else:
        print("Por favor, digite um número menor que 100.")
except ValueError:
    print("Por favor, digite apenas números válidos.")
