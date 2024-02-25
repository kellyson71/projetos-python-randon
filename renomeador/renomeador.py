import os
import json

# Caminho para a pasta contendo as pastas dos estagiários
caminho_pasta_estagiarios = 'C:\\Users\\kelly\\Desktop\\py\\renomeador\\media'

# Caminho para o arquivo JSON
caminho_arquivo_json = 'C:\\Users\\kelly\\Desktop\\py\\renomeador\\Candidato.Json'

# Função para remover pontos e traços do CPF
def formatar_cpf(cpf):
    return ''.join(filter(str.isdigit, cpf))

# Função para obter o nome completo e a área a partir do arquivo JSON
def obter_nome_e_area(cpf):
    cpf_formatado = formatar_cpf(cpf)
    with open(caminho_arquivo_json, 'r', encoding='utf-8') as arquivo_json:
        dados = json.load(arquivo_json)[2].get('data', [])
        for estagiario in dados:
            json_cpf_formatado = formatar_cpf(estagiario.get('cpf', ''))
            if json_cpf_formatado == cpf_formatado:
                nome_completo = estagiario.get('nome_completo', '')
                area = estagiario.get('area', '')
                return f"{nome_completo} - {area}"
    return None

# Função para obter o CPF a partir do nome completo e da área
def obter_cpf(nome_e_area):
    nome_completo, area = nome_e_area.split(' - ')
    with open(caminho_arquivo_json, 'r', encoding='utf-8') as arquivo_json:
        dados = json.load(arquivo_json)[2].get('data', [])
        for estagiario in dados:
            if estagiario.get('nome_completo', '') == nome_completo and estagiario.get('area', '') == area:
                return estagiario.get('cpf', '')
    return None

# Menu
while True:
    print("Menu:")
    print("1. Renomear do CPF para o Nome Completo e Área")
    print("2. Renomear do Nome Completo e Área para o CPF")
    print("0. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        # Renomear do CPF para o Nome Completo e Área
        for pasta in os.listdir(caminho_pasta_estagiarios):
            caminho_pasta = os.path.join(caminho_pasta_estagiarios, pasta)
            
            if os.path.isdir(caminho_pasta):
                # Obter o CPF da pasta
                cpf_estagiario = formatar_cpf(pasta)
                
                # Obter o nome completo e a área usando a função
                nome_e_area = obter_nome_e_area(cpf_estagiario)
                
                if nome_e_area:
                    # Construir o novo nome da pasta
                    novo_nome = os.path.join(caminho_pasta_estagiarios, nome_e_area)
                    
                    # Renomear a pasta
                    os.rename(caminho_pasta, novo_nome)
                    print(f'A pasta {pasta} foi renomeada para {nome_e_area}')
                else:
                    print(f'Não foi possível encontrar informações para o CPF {cpf_estagiario}')

    elif escolha == '2':
        # Renomear do Nome Completo e Área para o CPF
        for pasta in os.listdir(caminho_pasta_estagiarios):
            caminho_pasta = os.path.join(caminho_pasta_estagiarios, pasta)
            
            if os.path.isdir(caminho_pasta):
                # Obter o nome completo e a área da pasta
                nome_e_area = pasta
                
                # Obter o CPF usando a função
                cpf_estagiario = obter_cpf(nome_e_area)
                
                if cpf_estagiario:
                    # Construir o novo nome da pasta
                    novo_nome = os.path.join(caminho_pasta_estagiarios, cpf_estagiario)
                    
                    # Renomear a pasta
                    os.rename(caminho_pasta, novo_nome)
                    print(f'A pasta {pasta} foi renomeada para {cpf_estagiario}')
                else:
                    print(f'Não foi possível encontrar informações para {nome_e_area}')

    elif escolha == '0':
        break

    else:
        print("Opção inválida. Tente novamente.")
