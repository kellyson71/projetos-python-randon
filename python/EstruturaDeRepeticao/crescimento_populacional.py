populacao_A = 80000
taxa_A = 0.03
populacao_B = 200000
taxa_B = 0.015
anos = 0

while populacao_A < populacao_B:
    populacao_A *= (1 + taxa_A)
    populacao_B *= (1 + taxa_B)
    anos += 1

print(f"Serão necessários {anos} anos para a população do país A ultrapassar a população do país B.")
