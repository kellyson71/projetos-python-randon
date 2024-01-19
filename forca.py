import random

def escolher_palavra():
    palavras = ["python", "programacao", "desenvolvimento", "computador", "tecnologia", "inteligencia"]
    return random.choice(palavras)

def exibir_palavra_oculta(palavra, letras_certas):
    return ''.join(letra if letra in letras_certas else '_' for letra in palavra)

def jogar_forca():
    palavra_secreta = escolher_palavra()
    letras_certas = set()
    tentativas = 6

    print("Bem-vindo ao Jogo da Forca!")

    while tentativas > 0:
        palavra_oculta = exibir_palavra_oculta(palavra_secreta, letras_certas)
        print(f"Palavra: {palavra_oculta}")
        print(f"Tentativas restantes: {tentativas}")

        letra_tentativa = input("Digite uma letra: ")

        if letra_tentativa in letras_certas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if letra_tentativa in palavra_secreta:
            letras_certas.add(letra_tentativa)
            if set(palavra_secreta) == letras_certas:
                print(f"Parabéns! Você descobriu a palavra: {palavra_secreta}")
                break
        else:
            tentativas -= 1
            print("Letra incorreta. Tente novamente.")

    else:
        print(f"Você perdeu! A palavra era: {palavra_secreta}")

jogar_forca()
