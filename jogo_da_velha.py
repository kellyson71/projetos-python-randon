def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas, colunas e diagonais
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or all(tabuleiro[j][i] == jogador for j in range(3)):
            return True
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    return False

def jogar_jogo_da_velha():
    tabuleiro = [[" "]*3 for _ in range(3)]
    jogadores = ['X', 'O']
    jogador_atual = jogadores[0]

    print("Bem-vindo ao Jogo da Velha!")

    for _ in range(9):
        exibir_tabuleiro(tabuleiro)
        linha = int(input(f"Jogador {jogador_atual}, escolha a linha (1, 2, 3): ")) - 1
        coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (1, 2, 3): ")) - 1

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual

            if verificar_vitoria(tabuleiro, jogador_atual):
                exibir_tabuleiro(tabuleiro)
                print(f"Parabéns! Jogador {jogador_atual} venceu!")
                break

            jogador_atual = jogadores[1] if jogador_atual == jogadores[0] else jogadores[0]
        else:
            print("Posição já ocupada. Escolha novamente.")

    else:
        exibir_tabuleiro(tabuleiro)
        print("Empate! O jogo terminou sem vencedores.")

# Exemplo de uso
jogar_jogo_da_velha()
