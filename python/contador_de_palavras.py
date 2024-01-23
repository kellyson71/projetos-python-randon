def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)

# Exemplo de uso
texto = input("Digite um texto para contar as palavras: ")
quantidade_palavras = contar_palavras(texto)
print(f"O texto possui {quantidade_palavras} palavras.")
