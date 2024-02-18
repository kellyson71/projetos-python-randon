preco1 = float(input("Digite o preço do primeiro produto: "))
preco2 = float(input("Digite o preço do segundo produto: "))
preco3 = float(input("Digite o preço do terceiro produto: "))

mais_barato = min(preco1, preco2, preco3)

print(f"O produto mais barato custa R$ {mais_barato:.2f}")
