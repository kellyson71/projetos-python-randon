limite_peso = 50
peso_peixes = float(input("Digite o peso de peixes em quilos: "))

if peso_peixes > limite_peso:
    excesso = peso_peixes - limite_peso
    multa = excesso * 4
    print(f"Excesso de peso: {excesso} kg")
    print(f"Multa a ser paga: R$ {multa:.2f}")
else:
    print("Dentro do limite de peso. Sem multa.")
