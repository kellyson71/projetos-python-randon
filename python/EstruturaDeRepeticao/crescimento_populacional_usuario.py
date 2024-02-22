populacao_A = float(input("Digite a população do país A: "))
taxa_A = float(input("Digite a taxa de crescimento do país A (em decimal): "))
populacao_B = float(input("Digite a população do país B: "))
taxa_B = float(input("Digite a taxa de crescimento do país B (em decimal): "))
anos = 0

while populacao_A < populacao_B:
    populacao_A *= (1 + taxa_A)
    populacao_B *= (1 + taxa_B)
    anos += 1

print(f"Serão necessários {anos} anos para a população do país A ultrapassar a população do país B.")
