def minimax_with_heuristic(board, player):
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
            score = evaluate(board, player)
            score += minimax_with_heuristic(board, "X")
            board[move] = " "  # Undo the move
            if score > best_score:
                best_score = score
                best_move = move
    else:  # Minimizing player
        best_score = float("inf")
        for move in available_moves:
            board[move] = player
            score = evaluate(board, player)
            score += minimax_with_heuristic(board, "O")
            board[move] = " "  # Undo the move
            if score < best_score:
                best_score = score
                best_move = move

    return best_move

def evaluate(board, player):
    # Evaluate the board based on the current player
    if check_winner(board, player):
        return 1
    elif check_winner(board, get_opponent(player)):
        return -1
    else:
        return 0

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

def count_open_winning_paths(board, player):
    # Count the number of open paths to win for the current player
    count = 0
    for path in get_winning_paths():
        if all(board[i] == player or board[i] == " " for i in path):
            count += 1
    return count

def get_winning_paths():
    # Define the winning paths in Tic Tac Toe
    return [(0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)]

def heuristic_customization(board, player):
    # Add your custom heuristic features here
    return count_open_winning_paths(board, player)

# Modify the evaluate function to incorporate the custom heuristic
def evaluate(board, player):
    # Evaluate the board based on the current player and custom heuristics
    if check_winner(board, player):
        return 1
    elif check_winner(board, get_opponent(player)):
        return -1
    else:
        return heuristic_customization(board, player)
