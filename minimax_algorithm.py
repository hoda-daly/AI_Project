def minimax(board, player):
    available_moves = [i for i in range(9) if board[i] == " "]

    if check_winner(board, "X"):
        return -1
    elif check_winner(board, "O"):
        return 1
    elif not available_moves:
        return 0

    best_move = None
    if player == "O":  # Maximizing player
        best_score = float("-inf")
        for move in available_moves:
            board[move] = player
            score = minimax(board, "X")
            board[move] = " "  # Undo the move
            if score > best_score:
                best_score = score
                best_move = move
    else:  # Minimizing player
        best_score = float("inf")
        for move in available_moves:
            board[move] = player
            score = minimax(board, "O")
            board[move] = " "  # Undo the move
            if score < best_score:
                best_score = score
                best_move = move

    return best_move

def check_winner(board, player):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False
