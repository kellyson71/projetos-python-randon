vetor = []

for _ in range(10):
    caractere = input("Digite um caractere: ")
    vetor.append(caractere)

consoantes = [c for c in vetor if c.isalpha() and c.lower() not in 'aeiou']
print(f"Número de consoantes: {len(consoantes)}")
print(f"Consoantes: {consoantes}")
