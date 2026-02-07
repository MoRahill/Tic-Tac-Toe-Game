"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    
    # X starts first, so if equal counts, X plays
    return X if x_count == o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_moves.add((i, j))
    
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    
    # Check if action is valid
    if board[i][j] != EMPTY:
        raise ValueError("Invalid action")
    
    # Create a copy of the board
    new_board = [row[:] for row in board]
    new_board[i][j] = player(board)
    
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check all rows
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]
    
    # Check all columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Game over if there's a winner
    if winner(board) is not None:
        return True
    
    # Game over if no empty cells
    for row in board:
        if EMPTY in row:
            return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    current_player = player(board)
    
    if current_player == X:
        # X is maximizing
        best_score = -math.inf
        best_move = None
        
        for action in actions(board):
            score = min_play(result(board, action), -math.inf, math.inf)
            if score > best_score:
                best_score = score
                best_move = action
        
        return best_move
    else:
        # O is minimizing
        best_score = math.inf
        best_move = None
        
        for action in actions(board):
            score = max_play(result(board, action), -math.inf, math.inf)
            if score < best_score:
                best_score = score
                best_move = action
        
        return best_move


def max_play(board, alpha, beta):
    """
    Returns the maximum utility value for the maximizing player.
    """
    if terminal(board):
        return utility(board)
    
    value = -math.inf
    
    for action in actions(board):
        value = max(value, min_play(result(board, action), alpha, beta))
        alpha = max(alpha, value)
        
        # Prune if beta cutoff
        if alpha >= beta:
            break
    
    return value


def min_play(board, alpha, beta):
    """
    Returns the minimum utility value for the minimizing player.
    """
    if terminal(board):
        return utility(board)
    
    value = math.inf
    
    for action in actions(board):
        value = min(value, max_play(result(board, action), alpha, beta))
        beta = min(beta, value)
        
        # Prune if alpha cutoff
        if beta <= alpha:
            break
    
    return value
