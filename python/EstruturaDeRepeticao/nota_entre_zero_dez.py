while True:
    nota = float(input("Digite uma nota entre zero e dez: "))
    if 0 <= nota <= 10:
        break
    else:
        print("Nota inválida. Tente novamente.")

print(f"Você digitou a nota {nota}")
    