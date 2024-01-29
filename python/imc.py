def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC) com base no peso e altura.
    Formula: IMC = peso / altura^2
    """
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    """
    Classifica o IMC em categorias com base nos padrões comuns.
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade Grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade Grau 2"
    else:
        return "Obesidade Grau 3"

def main():
    print("Calculadora de Índice de Massa Corporal (IMC)")

    # Obter entrada do usuário
    peso = float(input("Digite seu peso em quilogramas: "))
    altura = float(input("Digite sua altura em metros: "))

    # Calcular IMC
    imc = calcular_imc(peso, altura)

    # Classificar o IMC
    classificacao = classificar_imc(imc)

    # Exibir resultados
    print(f"Seu IMC é: {imc:.2f}")
    print(f"Classificação: {classificacao}")

if __name__ == "__main__":
    main()
