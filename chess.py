BLACK_ROOK = "♜"
BLACK_KNIGHT = "♞"
BLACK_BISHOP = "♝"
BLACK_QUEEN = "♛"
BLACK_KING = "♚"
BLACK_PAWN = "♟"
WHITE_ROOK = "♖"
WHITE_KNIGHT = "♘"
WHITE_BISHOP = "♗"
WHITE_QUEEN = "♕"
WHITE_KING = "♔"
WHITE_PAWN = "♙"
EMPTY = " "

WHITE_PIECES = {WHITE_PAWN, WHITE_BISHOP, WHITE_KNIGHT, WHITE_ROOK, WHITE_QUEEN, WHITE_KING}
BLACK_PIECES = {BLACK_PAWN, BLACK_BISHOP, BLACK_KNIGHT, BLACK_ROOK, BLACK_QUEEN, BLACK_KING}

PIECE_SYMBOLS = {
    'r': BLACK_ROOK,
    'n': BLACK_KNIGHT,
    'b': BLACK_BISHOP,
    'q': BLACK_QUEEN,
    'k': BLACK_KING,
    'p': BLACK_PAWN,
    'R': WHITE_ROOK,
    'N': WHITE_KNIGHT,
    'B': WHITE_BISHOP,
    'Q': WHITE_QUEEN,
    'K': WHITE_KING,
    'P': WHITE_PAWN,
}

STARTING_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

def board_from_fen(fen):
    board = []
    
    rows = fen.split('/')
    
    for row in rows:
        
        board_row = []
        
        for char in row:
            if char.isdigit():
                board_row.extend([EMPTY] * int(char))
            else:
                board_row.append(PIECE_SYMBOLS[char])
                
        board.append(board_row)
                
    return board
    
    
def format_board(board):
    column_labels = '  a b c d e f g h'
    formatted_board = [column_labels]
    formatted_board.append(' +-----------------+')
    
    for i, row in enumerate(board):
        formatted_board.append(f"{8 - i}| {' '.join(row)} |")
    
    formatted_board.append(' +-----------------+')
    formatted_board.append(column_labels)
    
    return "\n".join(formatted_board)


def square_to_indices(square):
    column, row = square
    row_index = 8 - int(row)
    col_index = ord(column) - ord('a')
    return row_index, col_index

def validate_move(current_board_fen, starting_square, target_square, active_colour):
    
    #Validate that the move is well-formed
    if starting_square == target_square:
        return False
    
    if len(starting_square) != 2 or len(target_square) != 2:
        return False
    
    starting_square_indices = square_to_indices(starting_square)
    target_square_indices = square_to_indices(target_square)
    
    #Rewrite this using range
    if int(starting_square_indices[0]) > 7 or int(starting_square_indices[1] > 7):
        return False
    
    if int(starting_square_indices[0]) < 0 or int(starting_square_indices[1] < 0):
        return False
    
    if int(target_square_indices[0]) > 7 or int(target_square_indices[1] > 7):
        return False
    
    if int(target_square_indices[0]) < 0 or int(target_square_indices[1] < 0):
        return False
    
    current_board = board_from_fen(current_board_fen)
    
    starting_square_piece = current_board[starting_square_indices[0]][starting_square_indices[1]]
    target_square_piece = current_board[target_square_indices[0]][target_square_indices[1]]
    
    if starting_square_piece == EMPTY:
        return False
    
    if active_colour == 'w':
        if starting_square_piece in BLACK_PIECES:
            return False
        
        if target_square_piece in WHITE_PIECES:
            return False
    
    if active_colour == 'b':
        if starting_square_piece in WHITE_PIECES:
            return False
        
        if target_square_piece in BLACK_PIECES:
            return False
        
    if starting_square_piece == WHITE_PAWN:
        #Cannot change file unless capturing
        if target_square_piece == EMPTY and starting_square_indices[1] != target_square_indices[1]:
            return False
        #Cannot capture on 2 forward move
        if target_square_piece != EMPTY and starting_square_indices[1] != target_square_indices[1] and starting_square_indices[0] - target_square_indices[0] != 1:
            return False
        #Cannot move 2 forward unless on starting rank
        if starting_square_indices[0] - target_square_indices[0] > 2:
            return False
        #Cannot move more than 1 forward otherwise
        if starting_square_indices[0] - target_square_indices[0] > 1 and starting_square_indices[0] != 6:
            return False
        #Cannot move backwards
        if starting_square_indices[0] < target_square_indices[0]:
            return False
        
        
    
    print(current_board[starting_square_indices[0]][starting_square_indices[1]], current_board[target_square_indices[0]][target_square_indices[1]])
    
    print(starting_square, target_square, starting_square_indices, target_square_indices)
    
    return True
