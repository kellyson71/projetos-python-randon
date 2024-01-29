import json
import tkinter as tk
from tkinter import ttk

def carregar_filmes():
    try:
        with open("filmes.json", "r", encoding="utf-8") as file:
            filmes = json.load(file)
    except FileNotFoundError:
        filmes = []
    return filmes

def salvar_filmes(filmes):
    with open("filmes.json", "w", encoding="utf-8") as file:
        json.dump(filmes, file, indent=2)

def obter_recomendacoes(genero):
    filmes = carregar_filmes()
    recomendacoes = [filme for filme in filmes if filme["genero"] == genero and filme.get("avaliacao") is None]
    return recomendacoes

def atualizar_lista():
    genero_selecionado = combo_genero.get()
    recomendacoes = obter_recomendacoes(genero_selecionado)
    lista.delete(0, tk.END)
    for filme in recomendacoes:
        lista.insert(tk.END, f"{filme['titulo']} ({filme['ano']}) - Avaliação: {filme.get('avaliacao', 'Não avaliado')}")

def avaliar_filme():
    selecao = lista.curselection()
    if selecao:
        filme_selecionado = lista.get(selecao[0])
        filme_id = int(filme_selecionado.split()[0])
        avaliacao = float(entry_avaliacao.get())
        filmes = carregar_filmes()
        for filme in filmes:
            if filme["id"] == filme_id:
                filme["avaliacao"] = avaliacao
        salvar_filmes(filmes)
        atualizar_lista()

root = tk.Tk()
root.title("Recomendação de Filmes")

generos = ["Ação", "Comédia", "Drama", "Ficção Científica", "Romance", "Suspense", "Animação", "Documentário", "Outro"]
combo_genero = ttk.Combobox(root, values=generos)
combo_genero.set("Selecione o Gênero")
combo_genero.grid(row=0, column=0, padx=10, pady=10)

btn_atualizar = ttk.Button(root, text="Atualizar Lista", command=atualizar_lista)
btn_atualizar.grid(row=0, column=1, padx=10, pady=10)

lista = tk.Listbox(root, height=10, width=50)
lista.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

tk.Label(root, text="Avaliação (0-5):").grid(row=2, column=0, padx=10, pady=5)
entry_avaliacao = tk.Entry(root)
entry_avaliacao.grid(row=2, column=1, padx=10, pady=5)

btn_avaliar = ttk.Button(root, text="Avaliar Filme", command=avaliar_filme)
btn_avaliar.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
