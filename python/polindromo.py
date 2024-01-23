def verificar_palindromo(texto):
    texto = texto.lower().replace(" ", "").replace(",", "").replace(".", "")
    return texto == texto[::-1]

entrada = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")

if verificar_palindromo(entrada):
    print(f"'{entrada}' é um palíndromo!")
else:
    print(f"'{entrada}' não é um palíndromo.")
