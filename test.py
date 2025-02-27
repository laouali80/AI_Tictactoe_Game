import tictactoe as tt


X = "X"
O = "O"
EMPTY = None

# Initial empty board
board = [
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY]
]

# Board with X about to win
board2 = [
    [X, O, X],
    [O, X, O],
    [EMPTY, EMPTY, EMPTY]
]

# Board with O about to win
board3 = [
    [O, X, O],
    [X, O, X],
    [EMPTY, EMPTY, EMPTY]
]

# Test the minimax function
optimal_action = tt.minimax(board)
print(f"Optimal action: {optimal_action}")



# Test winner function
board = [
    [X, O, X],
    [O, X, O],
    [O, X, X]
]
print(f"Winner: {tt.winner(board)}")  # Expected: X

# Test terminal function
board = [
    [X, O, X],
    [O, X, O],
    [O, X, X]
]
print(f"Terminal: {tt.terminal(board)}")  # Expected: True

# Test utility function
board = [
    [X, O, X],
    [O, X, O],
    [O, X, X]
]
print(f"Utility: {tt.utility(board)}")  # Expected: 1

# Test isDraw function
board = [
    [X, O, X],
    [O, X, O],
    [O, X, O]
]
print(f"Is Draw: {tt.isDraw(board)}")  # Expected: True