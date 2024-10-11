def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

try:
    numero = int(input("Digite um número inteiro: "))
    
    resultado = verificar_par_impar(numero)
    print(f"O número {numero} é {resultado}.")
except ValueError:
    print("Por favor, digite apenas números inteiros válidos.")
