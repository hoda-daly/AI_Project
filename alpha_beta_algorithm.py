def alpha_beta_pruning(board, player, alpha=float("-inf"), beta=float("inf")):
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
            score = minimax_with_alpha_beta_pruning(board, "X", alpha, beta)
            board[move] = " "  # Undo the move
            if score > best_score:
                best_score = score
                best_move = move
            alpha = max(alpha, best_score)
            if alpha >= beta:
                break
    else:  # Minimizing player
        best_score = float("inf")
        for move in available_moves:
            board[move] = player
            score = minimax_with_alpha_beta_pruning(board, "O", alpha, beta)
            board[move] = " "  # Undo the move
            if score < best_score:
                best_score = score
                best_move = move
            beta = min(beta, best_score)
            if alpha >= beta:
                break

    return best_move

def minimax_with_alpha_beta_pruning(board, player, alpha, beta):
    available_moves = [i for i in range(9) if board[i] == " "]

    if check_winner(board, "X"):
        return -1
    elif check_winner(board, "O"):
        return 1
    elif not available_moves:
        return 0

    if player == "O":  # Maximizing player
        best_score = float("-inf")
        for move in available_moves:
            board[move] = player
            score = minimax_with_alpha_beta_pruning(board, "X", alpha, beta)
            board[move] = " "  # Undo the move
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if alpha >= beta:
                break
        return best_score
    else:  # Minimizing player
        best_score = float("inf")
        for move in available_moves:
            board[move] = player
            score = minimax_with_alpha_beta_pruning(board, "O", alpha, beta)
            board[move] = " "  # Undo the move
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if alpha >= beta:
                break
        return best_score

def check_winner(board, player):
    # Check if the current player has won
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]

    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False









#///////////////////////////////////////////////////////////////////////////////

