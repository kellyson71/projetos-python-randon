from textblob import TextBlob

def analisar_sentimentos(texto):
    blob = TextBlob(texto)
    polaridade = blob.sentiment.polarity

    if polaridade > 0:
        return 'Positivo'
    elif polaridade < 0:
        return 'Negativo'
    else:
        return 'Neutro'

# Exemplo de uso
texto = "Python é uma linguagem de programação incrível!"
sentimento = analisar_sentimentos(texto)
print(f"Sentimento: {sentimento}")
