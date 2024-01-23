import random
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Exemplo de uso
tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
nova_senha = gerar_senha(tamanho_senha)
print("Senha Gerada:", nova_senha)
