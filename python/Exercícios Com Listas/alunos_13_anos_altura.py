idades = []
alturas = []

for _ in range(30):
    idade = int(input("Digite a idade do aluno: "))
    altura = float(input("Digite a altura do aluno: "))
    idades.append(idade)
    alturas.append(altura)

media_alturas = sum(alturas) / len(alturas)
alunos_acima_13_abaixo_media = sum(1 for i in range(30) if idades[i] > 13 and alturas[i] < media_alturas)

print(f"Número de alunos com mais de 13 anos e altura abaixo da média: {alunos_acima_13_abaixo_media}")
