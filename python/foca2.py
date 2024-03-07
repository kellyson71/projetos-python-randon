import random

def escolher_palavra():
    palavras = ["python", "programacao", "desenvolvimento", "criptografia"]
    return random.choice(palavras)

def jogar_forca():
    palavra = escolher_palavra()
    tentativas = 6
    letras_corretas = set()

    while tentativas > 0:
        letra = input("Digite uma letra: ")

        if letra in palavra:
            letras_corretas.add(letra)
            print("Correto! Letras corretas:", " ".join(letras_corretas))
        else:
            tentativas -= 1
            print("Incorreto! Tentativas restantes:", tentativas)

        if set(palavra) == letras_corretas:
            print("Parabéns! Você venceu!")
            break

    else:
        print("Game Over. A palavra era:", palavra)

jogar_forca()
