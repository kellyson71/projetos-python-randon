import random

def gera_caca_palavras(palavras):
    tamanho = 10
    grade = [[' ' for _ in range(tamanho)] for _ in range(tamanho)]

    for palavra in palavras:
        adicionada = False
        while not adicionada:
            direcao = random.choice(['horizontal', 'vertical', 'diagonal'])
            if direcao == 'horizontal':
                coluna = random.randint(0, tamanho - len(palavra))
                linha = random.randint(0, tamanho - 1)
                if all(grade[linha][coluna+i] == ' ' for i in range(len(palavra))):
                    for i in range(len(palavra)):
                        grade[linha][coluna+i] = palavra[i]
                    adicionada = True
            elif direcao == 'vertical':
                coluna = random.randint(0, tamanho - 1)
                linha = random.randint(0, tamanho - len(palavra))
                if all(grade[linha+i][coluna] == ' ' for i in range(len(palavra))):
                    for i in range(len(palavra)):
                        grade[linha+i][coluna] = palavra[i]
                    adicionada = True
            elif direcao == 'diagonal':
                coluna = random.randint(0, tamanho - len(palavra))
                linha = random.randint(0, tamanho - len(palavra))
                if all(grade[linha+i][coluna+i] == ' ' for i in range(len(palavra))):
                    for i in range(len(palavra)):
                        grade[linha+i][coluna+i] = palavra[i]
                    adicionada = True

    return grade

def exibe_caca_palavras(grade):
    for linha in grade:
        print(' '.join(linha))

# Entrada do usuário para escolher as palavras
quantidade_palavras = int(input("Quantas palavras você quer incluir no caça-palavras? "))
palavras = []
for i in range(quantidade_palavras):
    palavra = input(f"Digite a palavra {i + 1}: ")
    palavras.append(palavra)

caca_palavras = gera_caca_palavras(palavras)
exibe_caca_palavras(caca_palavras)
