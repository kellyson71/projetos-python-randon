import random

def simular_lancamento_dados():
    return random.randint(1, 6)

# Exemplo de uso
quantidade_lancamentos = int(input("Digite a quantidade de lançamentos desejada: "))

for _ in range(quantidade_lancamentos):
    resultado = simular_lancamento_dados()
    print(f"Resultado do dado: {resultado}")
