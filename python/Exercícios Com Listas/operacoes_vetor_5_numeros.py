vetor = []

for _ in range(5):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)

soma = sum(vetor)
multiplicacao = 1
for num in vetor:
    multiplicacao *= num

print(f"Vetor: {vetor}")
print(f"Soma: {soma}")
print(f"Multiplicação: {multiplicacao}")
