import sys
import os

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

ongoing = True
winner = None;
current_player = "X"


def displayMap():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play():
    # displayMap();

    while ongoing:
        turn(current_player)
        check_game_over()
        tie()
        change()
        sys.stdin.read(1)
        # os.system("clear")

    displayMap()
    if winner == "X" or winner == "O":
        print(winner + " won");
    else:
        print("Tie")


def turn(player):
    displayMap();
    position = int(input("Choose 1-9: "))
    position = position - 1
    board[position] = player


def change():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


def check_game_over():
    # if there's a winner
    # Row
    global winner
    win_by_row = rows()
    win_by_col = col()
    win_by_diagonal = diagonal()

    if win_by_row:
        winner = win_by_row
    elif win_by_col:
        winner = win_by_col
    elif win_by_diagonal:
        winner = win_by_diagonal
    else:
        winner = None
    return


def tie():
    global ongoing
    if "-" not in board:
        ongoing = False
    return


def rows():
    global ongoing
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        ongoing = False;
    if row1:
        return board[0];
    elif row2:
        return board[3];
    elif row3:
        return board[6];
    return


def col():
    global ongoing
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    if col1 or col2 or col3:
        ongoing = False;
    if col1:
        return board[0];
    elif col2:
        return board[1];
    elif col3:
        return board[2];
    return


def diagonal():
    global ongoing
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"
    if diagonal1 or diagonal2:
        ongoing = False;
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]


play();