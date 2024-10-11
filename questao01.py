def somar(num1, num2):
    return num1 + num2

try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    
    resultado = somar(numero1, numero2)
    print(f"A soma de {numero1} e {numero2} é: {resultado}")
except ValueError:
    print("Por favor, digite apenas números válidos.")
