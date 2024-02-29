vetor1 = [int(input(f"Digite o elemento {i + 1} do primeiro vetor: ")) for i in range(10)]
vetor2 = [int(input(f"Digite o elemento {i + 1} do segundo vetor: ")) for i in range(10)]
vetor3 = [int(input(f"Digite o elemento {i + 1} do terceiro vetor: ")) for i in range(10)]

vetor_intercalado = [elem for triple in zip(vetor1, vetor2, vetor3) for elem in triple]
print(f"Vetor Intercalado: {vetor_intercalado}")
