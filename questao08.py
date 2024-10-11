def fibonacci(n):
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        proximo = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(proximo)
    return fib_seq[:n]


try:
    numero = int(input("Digite quantos termos da sequência de Fibonacci você deseja: "))
    
    if numero <= 0:
        print("Por favor, digite um número inteiro positivo.")
    else:
        sequencia = fibonacci(numero)
        print(f"A sequência de Fibonacci com {numero} termos é: {sequencia}")
except ValueError:
    print("Por favor, digite apenas números inteiros válidos.")
