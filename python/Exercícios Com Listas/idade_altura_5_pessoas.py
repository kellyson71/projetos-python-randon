idades = []
alturas = []

for _ in range(5):
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura: "))
    idades.append(idade)
    alturas.append(altura)

idades.reverse()
alturas.reverse()

print(f"Idades na ordem inversa: {idades}")
print(f"Alturas na ordem inversa: {alturas}")
