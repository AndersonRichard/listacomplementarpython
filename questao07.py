def fatorial(n):
    if n < 0:
        return None  
    elif n == 0 or n == 1:
        return 1  
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

try:
    numero = int(input("Digite um número inteiro não negativo: "))
    
    if numero < 0:
        print("Por favor, digite um número inteiro não negativo.")
    else:
        resultado = fatorial(numero)
        print(f"O fatorial de {numero} é: {resultado}")
except ValueError:
    print("Por favor, digite apenas números inteiros válidos.")
