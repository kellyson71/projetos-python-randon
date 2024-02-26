vetor = []

for _ in range(10):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)

soma_quadrados = sum(num**2 for num in vetor)
print(f"Soma dos quadrados: {soma_quadrados}")
