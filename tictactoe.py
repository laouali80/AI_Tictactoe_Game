"""
Tic Tac Toe Player
"""
import copy
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
    x_moves = 0
    o_moves = 0

    # Count the number of X and O moves on the board
    for row in board:
        for cell in row:
            if cell == X:
                x_moves += 1
            elif cell == O:
                o_moves += 1

    # Determine whose turn it is
    if x_moves <= o_moves:
        return X  # X goes first or if the number of moves is equal
    else:
        return O  # O's turn if X has made more moves


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for row in range(len(board)):
        for cell in range(len(board)):
            if board[row][cell] == EMPTY:
                action = (row, cell)
                possible_actions.add(action)

    return possible_actions


def validate_action(board, action):
    """
    Returns whether an Action is valide or not.
    """
    # print(f"Action received: {action}")

    if board[action[0]][action[1]] is not None:
        return False  # Invalid action
    else:
        return True  # Valid action

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

     # Validate the action before proceeding
    if not validate_action(board, action):
        raise ValueError("Invalid action: The cell is already occupied.")

    # Get the player to play from the board
    player_to_play = player(board)

    # Copy the board to not alter it
    new_board = copy.deepcopy(board)

    # Set the player's move on the new board
    new_board[action[0]][action[1]] = player_to_play

    # Return the new board
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check rows
    for row in range(len(board)):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not EMPTY:
            return board[row][0]  # Return the player who won

    # Check columns
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not EMPTY:
            return board[0][col]  # Return the player who won

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]  # Return the player who won
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]  # Return the player who won

    # No winner
    return None


    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None or isDraw(board):
        return True
    return False

def isDraw(board):
    """
    Returns True if the game is a draw, False otherwise.
    """
    for row in range(len(board)):
        if EMPTY in board[row]:
            return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board) == X:
         _, action = MAX_VALUE(board)
    else:
         _, action = MIN_VALUE(board)

    return action

def MIN_VALUE(board):
    """
    Returns the minimal value of the board and its best move.
    """
    if terminal(board):
        # print(utility(board))
        return utility(board), None
 
    best_move = None
    
    v = 100

    for action in actions(board):
        # print(action)
        # v = min(v, MAX_VALUE(result(board, move)))
        new_value, _ = MAX_VALUE(result(board, action))
       

        if new_value < v:
            best_move = action
            v = new_value

    return v, best_move

def MAX_VALUE(board):
    """
    Returns the maximal value of the board and its best move.
    """
    if terminal(board):
        # print(utility(board), None)
        return utility(board) , None

    best_move = None
    
    v = -100
    for action in actions(board):
        # v = max(v, MIN_VALUE(result(board, move)))
        new_value, _ = MIN_VALUE(result(board, action))
        # print('max new: ', new_value, board, action)

        if new_value > v:
            best_move = action
            v = new_value

    return v, best_move
