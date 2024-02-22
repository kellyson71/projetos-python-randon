maior = float('-inf')

for _ in range(5):
    numero = float(input("Digite um número: "))
    if numero > maior:
        maior = numero

print(f"O maior número é {maior}")
