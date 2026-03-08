import random

board = [
    [1, 2, 3],
    [4, "X", 6],
    [7, 8, 9]
]

def display_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print("|   {}   |   {}   |   {}   |".format(row[0], row[1], row[2]))
        print("|       |       |       |")
        print("+-------+-------+-------+")

def make_list_of_free_fields(board):
    free = []
    for r in range(3):
        for c in range(3):
            if isinstance(board[r][c], int):
                free.append((r, c))
    return free

def enter_move(board):
    while True:
        move = int(input("Enter your move (1-9): "))
        for r in range(3):
            for c in range(3):
                if board[r][c] == move:
                    board[r][c] = "O"
                    return
        print("Invalid move, try again.")

def draw_move(board):
    free = make_list_of_free_fields(board)
    r, c = random.choice(free)
    board[r][c] = "X"

def victory_for(board, sign):
    for row in board:
        if row.count(sign) == 3:
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == sign:
            return True

    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True

    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True

    return False


while True:
    display_board(board)
    enter_move(board)

    if victory_for(board, "O"):
        display_board(board)
        print("You win!")
        break

    if not make_list_of_free_fields(board):
        display_board(board)
        print("Draw!")
        break

    draw_move(board)

    if victory_for(board, "X"):
        display_board(board)
        print("Computer wins!")
        break
