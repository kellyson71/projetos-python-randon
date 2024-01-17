import math

def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        raise ValueError("Não é possível dividir por zero.")
    return x / y

def potencia(x, y):
    return x ** y

def raiz_quadrada(x):
    if x < 0:
        raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
    return math.sqrt(x)

while True:
    print("Selecione a operação:")
    print("1. Adicionar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potenciação")
    print("6. Raiz Quadrada")
    print("7. Sair")

    escolha = input("Digite a escolha (1/2/3/4/5/6/7): ")

    if escolha == '7':
        print("Encerrando a calculadora. Até mais!")
        break

    if escolha in ('1', '2', '3', '4', '5', '6'):
        try:
            num1 = float(input("Digite o primeiro número: "))

            if escolha != '6':
                num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            continue

        try:
            if escolha == '1':
                resultado = adicionar(num1, num2)
            elif escolha == '2':
                resultado = subtrair(num1, num2)
            elif escolha == '3':
                resultado = multiplicar(num1, num2)
            elif escolha == '4':
                resultado = dividir(num1, num2)
            elif escolha == '5':
                resultado = potencia(num1, num2)
            elif escolha == '6':
                resultado = raiz_quadrada(num1)

            print(f"Resultado: {resultado}")

        except ValueError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

        novamente = input("Deseja fazer outra operação? (sim/não): ").lower()
        if novamente != "sim":
            print("Encerrando a calculadora. Até mais!")
            break
    else:
        print("Entrada inválida. Por favor, escolha uma opção válida.")
