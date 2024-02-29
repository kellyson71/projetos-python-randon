medias = []

for _ in range(10):
    notas = [float(input(f"Digite a nota {i + 1} do aluno: ")) for i in range(4)]
    media = sum(notas) / len(notas)
    medias.append(media)

aprovados = [media for media in medias if media >= 7.0]

print(f"Número de alunos aprovados: {len(aprovados)}")
