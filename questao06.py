import cmath 

def calcular_raizes(a, b, c):
    D = b**2 - 4*a*c
    raiz1 = (-b + cmath.sqrt(D)) / (2*a)
    raiz2 = (-b - cmath.sqrt(D)) / (2*a)
    return raiz1, raiz2


try:
    a = float(input("Digite o coeficiente a: "))
    b = float(input("Digite o coeficiente b: "))
    c = float(input("Digite o coeficiente c: "))
    
    if a == 0:
        print("O coeficiente 'a' deve ser diferente de zero.")
    else:
        raiz1, raiz2 = calcular_raizes(a, b, c)
        print(f"As raízes da equação são: {raiz1} e {raiz2}")
except ValueError:
    print("Por favor, digite apenas números válidos.")
