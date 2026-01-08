# noughts and crosses game

# 3x3 graph, "drawing board"
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


# function to print board as 3x3
def print_board(board) -> None:
    for line in board:
        print(line)
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
def run(board):
  moves = 9
  while moves > 0:
    print_board(board)
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

# Tests
assert has_won([["x", "x", "o"], ["", "o", "o"], ["x", "", ""]], "x") == False
assert has_won([["x", "x", "x"], ["", "o", ""], ["o", "o", ""]], "x") == True
assert has_won([["x", "o", "o"], ["x", "o", ""], ["x", "", ""]], "x") == True
assert has_won([["o", "x", "o"], ["x", "", ""], ["x", "o", ""]], "x") == False
assert has_won([["o", "x", "o"], ["x", "o", ""], ["x", "x", "o"]], "o") == True
assert has_won([["o", "x", "x"], ["o", "x", ""], ["x", "o", ""]], "x") == True

run(board)
