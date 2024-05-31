player = "X"

def bord():
    rows, cols = 3, 3
    arr = [[" " for _ in range(cols)] for _ in range(rows)]
    return arr

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 81)

def switch_player():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"

def make_move(board, row, col, player):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    else:
        return False

def winner(board):
    # Check alle rijen
    for row in board:
        if all(element == row[0] and element != " " for element in row):
            print("Winnaar is", row[0])
            return True
    
    # Check alle kolommen
    for col in range(3):
        if all(board[row][col] == board[0][col] and board[row][col] != " " for row in range(3)):
            print("Winnaar is", board[0][col])
            return True
    
    # Check de eerste diagonaal (van linksboven naar rechtsonder)
    if board[0][0] == board[1][1] == board[2][2] != " ":
        print("Winnaar is", board[0][0])
        return True
    
    # Check de tweede diagonaal (van rechtsboven naar linksonder)
    if board[0][2] == board[1][1] == board[2][0] != " ":
        print("Winnaar is", board[0][2])
        return True
   
    # Als geen van de voorwaarden hierboven wordt voldaan, is er geen winnaar
    return False

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def game():
    board = bord()
    while not winner(board) and not check_draw(board):
        print_board(board)
        row = int(input(f"Player {player}, enter row (0-2): "))
        col = int(input(f"Player {player}, enter col (0-2): "))
        if make_move(board, row, col, player):
            if winner(board):
                print_board(board)
                print(f"Winnaar is {player}")
                return
            elif check_draw(board):
                print_board(board)
                print("Het is een gelijkspel!")
                return
            switch_player()
        else:
            print("Ongeldige zet, probeer opnieuw.")

game()
