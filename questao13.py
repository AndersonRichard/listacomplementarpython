def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

try:
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    
    celsius = fahrenheit_para_celsius(fahrenheit)
    print(f"A temperatura em Celsius é: {celsius:.2f}°C")
except ValueError:
    print("Por favor, digite um número válido.")
