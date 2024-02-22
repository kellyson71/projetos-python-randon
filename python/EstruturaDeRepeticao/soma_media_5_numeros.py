soma = 0

for _ in range(5):
    numero = float(input("Digite um número: "))
    soma += numero

media = soma / 5

print(f"Soma dos números: {soma}")
print(f"Média dos números: {media}")
