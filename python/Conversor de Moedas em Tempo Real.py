import requests

def converter_moeda(valor, moeda_origem, moeda_destino):
    api_key = 'sua_api_key'
    url = f'https://api.exchangerate-api.com/v4/latest/{moeda_origem}'

    try:
        response = requests.get(url)
        data = response.json()
        taxa_cambio = data['rates'][moeda_destino]
        resultado = valor * taxa_cambio
        return resultado
    except Exception as e:
        print(f"Erro na conversão: {e}")
        return None

valor_origem = float(input("Digite o valor a ser convertido: "))
moeda_origem = input("Digite a moeda de origem (por exemplo, USD): ").upper()
moeda_destino = input("Digite a moeda de destino (por exemplo, EUR): ").upper()

resultado = converter_moeda(valor_origem, moeda_origem, moeda_destino)

if resultado is not None:
    print(f"{valor_origem} {moeda_origem} equivale a {resultado:.2f} {moeda_destino}")
