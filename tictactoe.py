from copy import deepcopy


# --- GAME LOGIC --- #
def draw_board(board):
    print(str(board[0]) + " | " + str(board[1]) + " | " + str(board[2]))
    print(str(board[3]) + " | " + str(board[4]) + " | " + str(board[5]))
    print(str(board[6]) + " | " + str(board[7]) + " | " + str(board[8]))


def is_valid_move(board, move):
    if board[move-1] == "X" or board[move-1] == "O":
        return False
    if move not in range(1, 10):
        return False
    return True


def play_move(board, move, player):
    if is_valid_move(board, move):
        board[move-1] = player
        return True
    return False


def get_available_moves(board):
    moves = []
    for cell in board:
        if cell == "X" or cell == "O":
            continue
        else:
            moves.append(cell)
    return moves


def is_win(board, player):
    # diagonal
    if (board[0] == board[4] == board[8] or board[2] == board[4] == board[6]) and board[4] == player:
        return True
    
    # horizontal
    for i in range(3):
        if board[3*i] == board[3*i+1] == board[3*i+2] == player:
            return True
    
    # vertical
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True


def is_tie(board):
    if not is_win(board, "X") or not is_win(board, "O"):
        available_moves = get_available_moves(board)
        return len(available_moves) == 0


# --- MINIMAX ALGORITHM --- #
def game_over(board):
    return is_win(board, "X") or is_win(board, "O") or len(get_available_moves(board)) == 0


def evaluate_board(board):
    if is_win(board, "X"):
        return 1
    elif is_win(board, "O"):
        return -1
    else:
        return 0
    

def minimax(board, is_maximizing):
    if game_over(board):
        return [evaluate_board(board), None]
    
    best_move = None
    
    if is_maximizing:
        player = "X"
        best_value = -float("Inf")
    else:
        player = "O"
        best_value = float("Inf")
    
    for move in get_available_moves(board):
        new_board = deepcopy(board)
        play_move(new_board, move, player)
        new_value = minimax(new_board, not is_maximizing)[0]

        if is_maximizing and new_value > best_value:
            best_move = move
            best_value = new_value
        if not is_maximizing and new_value < best_value:
            best_move = move
            best_value = new_value
    
    return [best_value, best_move]


def main():
    while True:
        board = list(range(1, 10))
        print("Would you like to start or let the AI start?")
        print("[1] I will start")
        print("[2] Let AI start")
        print("[Q] Quit")
        start_choice = input("> ")

        if int(start_choice) == 1:
            players_turn = True
            player = "X"
            ai = "O"
        elif int(start_choice) == 2:
            players_turn = False
            player = "O"
            ai = "X"
        else:
            return
            
        while True:
            draw_board(board)
            if players_turn:
                print("Make your move! (Enter a number from 1-9)")
                player_move = int(input("> "))
                if not play_move(board, player_move, player):
                    print("Invalid move! Try again!")
                    continue
            else:
                if ai == "X":
                    ai_move = minimax(board, True)[1]
                else:
                    ai_move = minimax(board, False)[1]
                print(f"AI played: {ai_move}")
                play_move(board, ai_move, ai)
            
            players_turn = not players_turn

            if is_win(board, player):
                print("You won!")
                draw_board(board)
                break
            elif is_win(board, ai):
                print("The AI has beaten you!")
                draw_board(board)
                break
            if is_tie(board):
                print("The game ended in a tie!")
                draw_board(board)
                break

main()