def heuristic_reduction(board, player):
    # Apply heuristic reduction to choose a move
    best_move = None
    best_score = float("-inf")

    for move in get_available_moves(board):
        board[move] = player
        score = evaluate(board, player)
        board[move] = " "  # Undo the move

        if score > best_score:
            best_score = score
            best_move = move

    return best_move

def evaluate(board, player):
    # Simple heuristic: prioritize winning moves, then blocking opponent, then center, then corners, and finally sides
    if check_winner(board, player):
        return 10
    elif check_winner(board, get_opponent(player)):
        return -10
    elif " " in board:
        return 0
    elif board[4] == " ":
        return 5
    elif any(board[i] == " " for i in [0, 2, 6, 8]):
        return 3
    else:
        return 1

def get_available_moves(board):
    # Get a list of available (empty) moves on the board
    return [i for i in range(9) if board[i] == " "]

def check_winner(board, player):
    # Check if the current player has won
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]

    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def get_opponent(player):
    # Return the opponent's symbol
    return "X" if player == "O" else "O"
