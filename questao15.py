def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)


try:
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    
    resultado = mdc(numero1, numero2)
    print(f"O MDC de {numero1} e {numero2} é: {resultado}")
except ValueError:
    print("Por favor, digite apenas números inteiros válidos.")
