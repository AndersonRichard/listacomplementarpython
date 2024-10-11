def area_triangulo(base, altura):
    return (base * altura) / 2

try:
    base = float(input("Digite a base do triângulo: "))
    altura = float(input("Digite a altura do triângulo: "))
    
    resultado = area_triangulo(base, altura)
    print(f"A área do triângulo é: {resultado}")
except ValueError:
    print("Por favor, digite apenas números válidos.")
