import math

def print_board(board):
    print(" ")
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print(" ")

def check_winner(board, player):
    # Check rows, columns, and diagonals
    win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for condition in win_conditions:
        if all(board[pos] == player for pos in condition):
            return True
    return False

def get_empty_positions(board):
    return [i for i in range(9) if board[i] == ' ']

def human_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move in get_empty_positions(board):
                return move
            else:
                print("Invalid move! Try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def robot_move(board):
    best_score = -math.inf
    best_move = None
    for move in get_empty_positions(board):
        board[move] = 'O'
        
        score = minimax(board, 0, False)
        board[move] = ' '
        if score > best_score:
            
            print(score)
            best_score = score
            best_move = move
    print("t")
    return best_move

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    elif check_winner(board, 'X'):
        return -1
    elif len(get_empty_positions(board)) == 0:
        return 0
    if is_maximizing:
        best_score = -math.inf
        for move in get_empty_positions(board):
            board[move] = 'O'
            score = minimax(board, depth + 1, False)
            board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_empty_positions(board):
            board[move] = 'X'
            score = minimax(board, depth + 1, True)
            board[move] = ' '
            best_score = min(score, best_score)
        return best_score

def play_game():
    board = [' '] * 9
    print("Welcome to Tic-Tac-Toe!")
    print_board([str(i + 1) for i in range(9)])
    human_symbol = 'X'
    robot_symbol = 'O'

    while True:
        # Human's turn
        human_position = human_move(board)
        board[human_position] = human_symbol
        print_board(board)
        if check_winner(board, human_symbol):
            print("Congratulations! You win!")
            break
        if len(get_empty_positions(board)) == 0:
            print("It's a tie!")
            break

        # Robot's turn
        robot_position = robot_move(board)
        board[robot_position] = robot_symbol
        print("Robot chooses position", robot_position + 1)
        print_board(board)
        if check_winner(board, robot_symbol):
            print("Sorry, you lose!")
            break
        if len(get_empty_positions(board)) == 0:
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()
