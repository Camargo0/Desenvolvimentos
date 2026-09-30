escolha = input("Escolha X ou O: ").strip().upper()

if escolha not in ("X", "O"):
    print("Escolha inválida. Por favor, escolha X ou O.")
    exit()

jogador_atual = escolha
tabuleiro = [" " for _ in range(9)]

def exibir_tabuleiro():
    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("--+---+--")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("--+---+--")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")


def verificar_vencedor():
    combinacoes_vencedoras = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in combinacoes_vencedoras:
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] != " ":
            return tabuleiro[a]

    if " " not in tabuleiro:
        return "Empate"

    return None

while True:
    exibir_tabuleiro()
    posicao = int(input(f"Jogador {jogador_atual}, digite a posição de 0 a 8: "))

    if posicao < 0 or posicao > 8:
        print("Posição inválida. Digite um número entre 0 e 8.")
        continue

    if tabuleiro[posicao] != " ":
        print("Essa casa já está ocupada. Tente outra.")
        continue

    tabuleiro[posicao] = jogador_atual

    vencedor = verificar_vencedor()
    if vencedor:
        exibir_tabuleiro()
        if vencedor == "Empate":
            print("O jogo empatou!")
        else:
            print(f"O jogador {vencedor} venceu!")
        break

    jogador_atual = "O" if jogador_atual == "X" else "X"

