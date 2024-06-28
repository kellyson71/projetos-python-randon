import os
import json

# Definindo os caminhos para as pastas e arquivos
caminho_pasta_estagiarios = 'C:\\Users\\kelly\Documents\\renomeador\\renomeador\\media'  
caminho_arquivo_json = 'C:\\Users\\kelly\\Documents\\renomeador\\renomeador\\Candidato.Json'  

# Definindo uma função para formatar o CPF
def formatar_cpf(cpf):
    return ''.join(filter(str.isdigit, cpf))  

# Definindo uma função para obter o nome completo e a área a partir do JSON
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

# Iterando sobre as pastas dos estagiários para renomear
pastas_nao_renomeadas = []  # Lista para armazenar pastas não renomeadas

for pasta in os.listdir(caminho_pasta_estagiarios):
    caminho_pasta = os.path.join(caminho_pasta_estagiarios, pasta)  
    
    if os.path.isdir(caminho_pasta):  
        cpf_estagiario = formatar_cpf(pasta)  
        nome_e_area = obter_nome_e_area(cpf_estagiario)  

        if nome_e_area:  
            novo_nome = os.path.join(caminho_pasta_estagiarios, nome_e_area)  
            try:
                os.rename(caminho_pasta, novo_nome)  
                print(f'A pasta {pasta} foi renomeada para {nome_e_area}')  
            except FileExistsError:
                pastas_nao_renomeadas.append(pasta)  # Adicionando pasta à lista de não renomeadas
                print(f'A pasta {pasta} não pôde ser renomeada, pois o nome já existe')
        else:
            pastas_nao_renomeadas.append(pasta)  # Adicionando pasta à lista de não renomeadas
            print(f'Não foi possível encontrar informações para o CPF {cpf_estagiario}')

# Imprimindo pastas não renomeadas
print("\nPastas não renomeadas ou repetidas:")
for pasta in pastas_nao_renomeadas:
    print(pasta)
