tamanho_arquivo = float(input("Digite o tamanho do arquivo para download em MB: "))
velocidade_internet = float(input("Digite a velocidade do link de Internet em Mbps: "))

tempo_download = (tamanho_arquivo / (velocidade_internet / 8)) / 60

print(f"\nO tempo aproximado de download do arquivo é: {tempo_download:.2f} minutos")
