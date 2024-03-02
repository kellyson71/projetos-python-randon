notas = []

for _ in range(4):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print(f"Notas: {notas}")
print(f"Média: {media}")
