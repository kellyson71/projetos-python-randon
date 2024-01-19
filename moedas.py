import requests

def obter_taxa_cambio(origem, destino):
    url = f"https://api.exchangerate-api.com/v4/latest/{origem}"
    resposta = requests.get(url)
    dados = resposta.json()
    taxa_cambio = dados["rates"][destino]
    return taxa_cambio

def converter_moeda(valor, origem, destino):
    taxa_cambio = obter_taxa_cambio(origem, destino)
    valor_convertido = valor * taxa_cambio
    return valor_convertido

# Exemplo de uso
valor_a_converter = float(input("Digite o valor a ser convertido: "))
moeda_origem = input("Digite a moeda de origem (código da moeda): ")
moeda_destino = input("Digite a moeda de destino (código da moeda): ")

resultado = converter_moeda(valor_a_converter, moeda_origem, moeda_destino)
print(f"{valor_a_converter} {moeda_origem} é equivalente a {resultado:.2f} {moeda_destino}")
