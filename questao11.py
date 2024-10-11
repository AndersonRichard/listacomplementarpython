def eh_palindromo(s):
    s = s.lower().replace(" ", "") 
    return s == s[::-1]  

string = input("Digite uma string: ")

if eh_palindromo(string):
    print(f'"{string}" é um palíndromo.')
else:
    print(f'"{string}" não é um palíndromo.')
