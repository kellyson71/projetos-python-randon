numeros = []

for _ in range(20):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]

print(f"Números: {numeros}")
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")
