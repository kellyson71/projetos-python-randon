class Nota:
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo

class AplicativoNotas:
    def __init__(self):
        self.notas = []

    def criar_nota(self, titulo, conteudo):
        nota = Nota(titulo, conteudo)
        self.notas.append(nota)

    def ler_notas(self):
        for nota in self.notas:
            print(f"Título: {nota.titulo}")
            print(f"Conteúdo: {nota.conteudo}")
            print("")

    def atualizar_nota(self, indice, novo_titulo, novo_conteudo):
        if indice >= 0 and indice < len(self.notas):
            nota = self.notas[indice]
            nota.titulo = novo_titulo
            nota.conteudo = novo_conteudo
            print("Nota atualizada com sucesso!")
        else:
            print("Índice inválido!")

    def excluir_nota(self, indice):
        if indice >= 0 and indice < len(self.notas):
            del self.notas[indice]
            print("Nota excluída com sucesso!")
        else:
            print("Índice inválido!")

# Exemplo de uso do aplicativo de notas
aplicativo = AplicativoNotas()

aplicativo.criar_nota("Compras", "1. Leite\n2. Ovos\n3. Pão")
aplicativo.criar_nota("Tarefas", "1. Limpar a casa\n2. Fazer exercícios\n3. Estudar")

aplicativo.ler_notas()

aplicativo.atualizar_nota(0, "Compras de mercado", "1. Leite\n2. Ovos\n3. Pão\n4. Frutas")
aplicativo.excluir_nota(1)

aplicativo.ler_notas()