import random

# Função para imprimir o tabuleiro
def print_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

# Função para verificar se alguém ganhou
def check_winner(board, player):
    # Verificar linhas, colunas e diagonais
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# Função para verificar empate
def check_draw(board):
    return all(isinstance(board[i][j], str) for i in range(3) for j in range(3))

# Função para verificar se o movimento é válido
def valid_move(board, move):
    return 1 <= move <= 9 and isinstance(board[(move - 1) // 3][(move - 1) % 3], int)

# Função para atualizar o tabuleiro com o movimento
def make_move(board, move, player):
    board[(move - 1) // 3][(move - 1) % 3] = player

# Função principal do jogo
def play_game():
    # Inicializando o tabuleiro
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    player = "O"  # O jogador humano
    computer = "X"  # O computador
    game_over = False

    # O computador faz o primeiro movimento no meio
    make_move(board, 5, computer)
    print_board(board)

    # Loop principal do jogo
    while not game_over:
        # Jogada do usuário
        move = None
        while move is None or not valid_move(board, move):
            try:
                move = int(input(f"Digite seu movimento (1-9): "))
                if not valid_move(board, move):
                    print("Movimento inválido. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número de 1 a 9.")

        make_move(board, move, player)
        print_board(board)

        # Verifica se o jogador ganhou
        if check_winner(board, player):
            print("Você ganhou!")
            break
        elif check_draw(board):
            print("Empate!")
            break

        # Jogada do computador
        available_moves = [board[i][j] for i in range(3) for j in range(3) if isinstance(board[i][j], int)]
        move = random.choice(available_moves)
        make_move(board, move, computer)
        print("Movimento do computador:")
        print_board(board)

        # Verifica se o computador ganhou
        if check_winner(board, computer):
            print("O computador ganhou!")
            break
        elif check_draw(board):
            print("Empate!")
            break

# Inicia o jogo
play_game()
