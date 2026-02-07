The game follows the classic 3×3 Tic‑Tac‑Toe rules. Two players, X and O, take turns marking empty squares on the board. The objective is to place three identical symbols in a row horizontally, vertically, or diagonally. The game ends when a player wins or when the board is full, resulting in a tie.

Game Logic
Board Representation
The board is stored as a 3×3 list. Each cell contains:

"X" for player X

"O" for player O

None for an empty cell

Turn Selection
The current player is determined by counting the number of X’s and O’s on the board. If both counts are equal, X plays next; otherwise, O plays.

Valid Moves
All empty cells are returned as possible actions. Each action is represented as a pair of coordinates (i, j).

Resulting Board
A new board state is generated after applying a move. The original board is never modified directly.

Winner Detection
The game checks:

All rows

All columns

Both diagonals

If any contain the same non‑empty symbol three times, that symbol is declared the winner.

Terminal State
A board is terminal if:

A player has won

No empty cells remain

Utility Values
Utility values are used by the AI:

1 if X wins

-1 if O wins

0 for a tie

AI Logic: Minimax and Alpha‑Beta Pruning
Minimax Algorithm
The AI uses the Minimax algorithm to evaluate all possible future game states.

X is the maximizing player

O is the minimizing player

The algorithm recursively explores every possible move until reaching a terminal state

Each terminal state is assigned a utility value

The algorithm backtracks to choose the move that guarantees the best outcome

This ensures the AI always plays optimally and cannot be beaten.

Alpha‑Beta Pruning
Includes Alpha‑Beta pruning, which improves Minimax by eliminating branches that cannot affect the final decision.

Two values are tracked:

alpha: the best guaranteed score for the maximizing player

beta: the best guaranteed score for the minimizing player

Pruning occurs when:

alpha >= beta in the maximizing function

beta <= alpha in the minimizing function

This reduces the number of states explored and speeds up decision‑making without changing the final result.
