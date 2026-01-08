import argparse
import random

# noughts and crosses game

# 3x3 graph, "drawing board"
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


# function to print board as 3x3
def print_board(board) -> None:
    print("\n")
    print("  | 0 | 1 | 2 |")
    print("---------------")
    for idx, line in enumerate(board):
      print(f"{idx} | {line[0]} | {line[1]} | {line[2]} |")
      print("---------------")
    print("\n")

    return None


# function to check if X or O has won
def has_won(board, symbol: str) -> bool:
    # the rules for winning are either 3*symbol across, 3*symbol downward, or 3*symbol diagonal
    # across
    for line in board:
        if all([line[x] == symbol for x in range(3)]):
            return True

    # downward
    for i in range(3):
        if all([board[x][i] == symbol for x in range(3)]):
            return True

    # diagonal
      # board[0][0] board[1][1] board[2][2] [x][x]
      # board[0][2] board[1][1] board[2][0] [x][-x-1]
    if all([board[x][x] == symbol for x in range(3)]) or all([board[x][-x-1] == symbol for x in range(3)]):
      return True
    # if no winners found:
    return False

# function to input symbol into chosen row and column
def input_symbol(board:list,symbol:str,row:int,column:int) -> list:
    board[row][column] = symbol
    return board

# function to evaluate whether the chosen row and column are unoccupied
def is_valid_move(board, row, column) -> bool:
  try:
    row = int(row)
    column = int(column)
  except:
    return False
  if row > 2 or column > 2:
    return False
  return board[row][column] == " "

def input_row_column():
  row  = input("Input the row (down) you want (0, 1, 2): ")
  column = input("Input the column (along) you want (0, 1, 2): ")
  return row, column

# game loop
def run(board: list[list]) -> None:
  moves = 9
  print_board(board)
  while moves > 0:
    if moves % 2 == 0:
      symbol = "x"
    else:
      symbol = "o"
    print(f"Move belongs to {symbol.upper()}!")
    row, column = input_row_column()
    while not is_valid_move(board, row, column):
      row,column = input_row_column()
    row, column = int(row), int(column)
    board = input_symbol(board,symbol,row,column)
    print_board(board)
    print("Let's see...")
    if has_won(board, symbol):
      print(f"Indeed! {symbol.upper()} won!")
      return
    else:
      print("Must have been the wind...")
    moves -= 1

  print("The game is over, it seems nobody won! Try again soon.")

# vs computer loop (random.randint(0,2) until somehing sticks)
def run_vs_comp(board: list[list]):
  user_symbol = input("Do you want to be X or O? ").lower()
  while user_symbol not in ["x", "o"]:
    user_symbol = input("Do you want to be X or O? ")
  if user_symbol == "x":
    computer_symbol = "o"
  else:
    computer_symbol = "x"

  moves = 9
  print_board(board)
  while moves > 0:
    if moves % 2 != 0:
      print("Computer is thinking...")
      c_row, c_column = random.randint(0,2), random.randint(0,2)
      while not is_valid_move(board, c_row, c_column):
        c_row, c_column = random.randint(0,2), random.randint(0,2)
      board = input_symbol(board, computer_symbol, c_row, c_column)
      print_board(board)
      if has_won(board, computer_symbol):
        print("Computer won!")
        return
    else:
      u_row, u_column = input_row_column()
      while not is_valid_move(board, u_row, u_column):
        u_row,u_column = input_row_column()
      u_row, u_column = int(u_row), int(u_column)
      board = input_symbol(board,user_symbol,u_row,u_column)
      print_board(board)
      print("Let's see...")
      if has_won(board, user_symbol):
        print(f"You've won!")
        return
      else:
        print("Must have been the wind...")

    moves -= 1
  print("The game is over, it seems nobody won! Try again soon.")





# Tests
assert has_won([["x", "x", "o"], ["", "o", "o"], ["x", "", ""]], "x") == False
assert has_won([["x", "x", "x"], ["", "o", ""], ["o", "o", ""]], "x") == True
assert has_won([["x", "o", "o"], ["x", "o", ""], ["x", "", ""]], "x") == True
assert has_won([["o", "x", "o"], ["x", "", ""], ["x", "o", ""]], "x") == False
assert has_won([["o", "x", "o"], ["x", "o", ""], ["x", "x", "o"]], "o") == True
assert has_won([["o", "x", "x"], ["o", "x", ""], ["x", "o", ""]], "x") == True

# parser for computer/self play
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--computer", help="Play against computer.", action="store_true")
parser.add_argument("-s", "--self", help="Play against self.", action="store_true")
args = parser.parse_args()

if args.computer:
  run_vs_comp(board)
elif args.self:
  run(board)
else:
  decision = input("Would you like to play against yourself, a friend, or the computer? ")
  while decision.lower() not in ["myself", "computer", "friend"]:
    decision = input("Would you like to play against yourself, a friend, or the computer? ")
  if decision in ["myself", "friend"]:
    run(board)
  else:
    run_vs_comp(board)
