import tkinter as tk
from tkinter import ttk
import json

class RecomendadorFilmes:
    def __init__(self, root, filmes):
        self.root = root
        self.root.title("Recomendador de Filmes")

        self.filmes = filmes

        self.label_titulo = ttk.Label(root, text="Escolha um filme:")
        self.label_titulo.pack(pady=10)

        self.combobox_filmes = ttk.Combobox(root, values=[filme["titulo"] for filme in filmes], state="readonly")
        self.combobox_filmes.pack(pady=10)

        self.button_recomendar = ttk.Button(root, text="Recomendar", command=self.recomendar_filme)
        self.button_recomendar.pack(pady=10)

        self.label_resultado = ttk.Label(root, text="")
        self.label_resultado.pack(pady=10)

    def recomendar_filme(self):
        filme_selecionado = self.combobox_filmes.get()
        filme = next((f for f in self.filmes if f["titulo"] == filme_selecionado), None)

        if filme:
            avaliacao = filme["avaliacao"]
            genero = filme["genero"]
            recomendacoes = [f for f in self.filmes if f["genero"] == genero and f["avaliacao"] > avaliacao]

            if recomendacoes:
                recomendacao = min(recomendacoes, key=lambda x: x["avaliacao"])
                self.label_resultado.config(text=f"Recomendação: {recomendacao['titulo']} - Avaliação: {recomendacao['avaliacao']}")
            else:
                self.label_resultado.config(text="Não há recomendações disponíveis para este filme.")
        else:
            self.label_resultado.config(text="Filme não encontrado.")

def carregar_filmes_do_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            filmes_json = json.load(arquivo)
        return filmes_json
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return []

if __name__ == "__main__":
    nome_arquivo = "filmes.json"
    filmes_json = carregar_filmes_do_arquivo(nome_arquivo)

    if filmes_json:
        root = tk.Tk()
        app = RecomendadorFilmes(root, filmes_json)
        root.mainloop()
    else:
        print("Não foi possível carregar os filmes do arquivo.")
