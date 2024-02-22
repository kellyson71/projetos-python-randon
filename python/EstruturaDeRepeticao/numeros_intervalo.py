inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))

soma = 0
numeros = []

for numero in range(inicio, fim + 1):
    soma += numero
    numeros.append(numero)

print(f"Números no intervalo: {numeros}")
print(f"Soma dos números: {soma}")
