import json

def contar_candidatos_por_area(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados_json = json.load(arquivo)

        if isinstance(dados_json, list):
            contagem_areas = {}

            for item in dados_json:
                if 'area' in item:
                    area = item['area']
                    contagem_areas[area] = contagem_areas.get(area, 0) + 1

            for area, quantidade in contagem_areas.items():
                print(f"{area} -- {quantidade} candidato(s)")

        else:
            print("Formato do JSON não reconhecido. Esperava uma lista de objetos JSON.")

    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_arquivo}")
    except json.JSONDecodeError:
        print(f"Erro ao decodificar o arquivo JSON: {caminho_arquivo}")

contar_candidatos_por_area('Candidato.json')
print("foi")
