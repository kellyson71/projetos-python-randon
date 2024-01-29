# Importar as bibliotecas necessárias
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from tkinter import *

# Ler o arquivo JSON e converter em um dataframe
filmes = pd.read_json("filmes.json")

# Ler o conjunto de dados de filmes e avaliações
ratings = pd.read_csv("ratings.csv")
movies = pd.read_csv("movies.csv")

# Juntar os dois dataframes em um só, usando o id do filme como chave
data = pd.merge(ratings, movies, on="movieId")

# Calcular a média e o número de avaliações para cada filme
data["mean_rating"] = data.groupby("movieId")["rating"].transform("mean")
data["rating_count"] = data.groupby("movieId")["rating"].transform("count")

# Filtrar os filmes com pelo menos 50 avaliações
data = data[data["rating_count"] >= 50]

# Criar uma matriz esparsa de usuários e filmes, preenchendo com zero os valores faltantes
matrix = data.pivot_table(index="userId", columns="title", values="rating").fillna(0)

# Calcular a similaridade entre os filmes usando a distância cosseno
similarity = cosine_similarity(matrix.T)

# Criar um dataframe com os títulos dos filmes e as similaridades
similarity_df = pd.DataFrame(similarity, index=matrix.columns, columns=matrix.columns)

# Definir uma função que recebe o título de um filme e retorna os cinco filmes mais similares
def recommend(title):
    # Verificar se o filme está no dataframe
    if title in similarity_df.index:
        # Obter a série de similaridades para o filme
        series = similarity_df.loc[title]
        # Ordenar os filmes em ordem decrescente de similaridade
        series = series.sort_values(ascending=False)
        # Retornar os cinco primeiros filmes, excluindo o próprio filme
        return series[1:6]
    else:
        # Retornar uma mensagem de erro se o filme não for encontrado
        return "Filme não encontrado. Por favor, digite outro título."

# Criar uma interface gráfica usando o tkinter
window = Tk()
window.title("Recomendador de Filmes")
window.geometry("400x300")

# Criar um rótulo para o título do programa
label = Label(window, text="Recomendador de Filmes", font=("Arial", 20))
label.pack(pady=10)

# Criar uma variável para armazenar o título do filme digitado pelo usuário
title = StringVar()

# Criar uma caixa de entrada para o usuário digitar o título do filme
entry = Entry(window, textvariable=title)
entry.pack(pady=10)

# Criar uma função para mostrar as recomendações na tela
def show_recommendations():
    # Obter o título do filme da variável
    title = entry.get()
    # Limpar a caixa de entrada
    entry.delete(0, END)
    # Obter as recomendações usando a função definida anteriormente
    recommendations = recommend(title)
    # Verificar se as recomendações são válidas
    if isinstance(recommendations, pd.Series):
        # Criar uma lista vazia para armazenar os títulos dos filmes recomendados
        titles = []
        # Percorrer as recomendações e adicionar os títulos à lista
        for i in range(len(recommendations)):
            titles.append(recommendations.index[i])
        # Mostrar os títulos na tela, usando rótulos
        label1 = Label(window, text="Filmes recomendados para você:", font=("Arial", 15))
        label1.pack(pady=10)
        label2 = Label(window, text=titles[0], font=("Arial", 12))
        label2.pack(pady=5)
        label3 = Label(window, text=titles[1], font=("Arial", 12))
        label3.pack(pady=5)
        label4 = Label(window, text=titles[2], font=("Arial", 12))
        label4.pack(pady=5)
        label5 = Label(window, text=titles[3], font=("Arial", 12))
        label5.pack(pady=5)
        label6 = Label(window, text=titles[4], font=("Arial", 12))
        label6.pack(pady=5)
    else:
        # Mostrar a mensagem de erro na tela, usando um rótulo
        label7 = Label(window, text=recommendations, font=("Arial", 15), fg="red")
        label7.pack(pady=10)

# Criar um botão para o usuário clicar e ver as recomendações
button = Button(window, text="Ver recomendações", command=show_recommendations)
button.pack(pady=10)

# Executar o programa
window.mainloop()
