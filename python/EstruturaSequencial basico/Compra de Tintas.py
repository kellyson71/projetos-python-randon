import math

metros_quadrados = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

litros_necessarios = metros_quadrados / 3
latas_18litros = math.ceil(litros_necessarios / 18)
preco_total = latas_18litros * 80

print(f"Quantidade de latas de tinta de 18 litros: {latas_18litros}")
print(f"Preço total: R$ {preco_total:.2f}")


metros_quadrados = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

litros_necessarios = metros_quadrados / 6

latas_18litros = math.ceil(litros_necessarios / 18)
preco_latas = latas_18litros * 80

galoes_36litros = math.ceil(litros_necessarios / 3.6)
preco_galoes = galoes_36litros * 25

latas_mistura = int(litros_necessarios / 18)
resto = litros_necessarios % 18
galoes_mistura = math.ceil(resto / 3.6)

preco_mistura = (latas_mistura * 80) + (galoes_mistura * 25)

print(f"\nOpção 1: Comprar apenas latas de 18 litros")
print(f"Quantidade de latas de tinta de 18 litros: {latas_18litros}")
print(f"Preço total: R$ {preco_latas:.2f}")

print(f"\nOpção 2: Comprar apenas galões de 3,6 litros")
print(f"Quantidade de galões de tinta de 3,6 litros: {galoes_36litros}")
print(f"Preço total: R$ {preco_galoes:.2f}")

print("\nOpção 3: Misturar latas e galões")
print(f"Quantidade de latas de tinta de 18 litros: {latas_mistura}")
print(f"Quantidade de galões de tinta de 3,6 litros: {galoes_mistura}")
print(f"Preço total: R$ {preco_mistura:.2f}")
