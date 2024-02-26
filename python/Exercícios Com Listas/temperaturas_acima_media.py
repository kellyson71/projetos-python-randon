temperaturas = []

for mes in range(1, 13):
    temperatura = float(input(f"Digite a temperatura média do mês {mes}: "))
    temperaturas.append(temperatura)

media_anual = sum(temperaturas) / len(temperaturas)

acima_media = [(mes, temp) for mes, temp in enumerate(temperaturas, start=1) if temp > media_anual]

print(f"Meses com temperatura acima da média anual: {acima_media}")
