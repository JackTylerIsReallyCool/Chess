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

WHITE_PIECES = {
    WHITE_PAWN,
    WHITE_BISHOP,
    WHITE_KNIGHT,
    WHITE_ROOK,
    WHITE_QUEEN,
    WHITE_KING,
}
BLACK_PIECES = {
    BLACK_PAWN,
    BLACK_BISHOP,
    BLACK_KNIGHT,
    BLACK_ROOK,
    BLACK_QUEEN,
    BLACK_KING,
}

PIECE_SYMBOLS = {
    "r": BLACK_ROOK,
    "n": BLACK_KNIGHT,
    "b": BLACK_BISHOP,
    "q": BLACK_QUEEN,
    "k": BLACK_KING,
    "p": BLACK_PAWN,
    "R": WHITE_ROOK,
    "N": WHITE_KNIGHT,
    "B": WHITE_BISHOP,
    "Q": WHITE_QUEEN,
    "K": WHITE_KING,
    "P": WHITE_PAWN,
}

STARTING_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"


def decode_fen(fen):
    board = []

    rows = fen.split("/")

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
    column_labels = "  a b c d e f g h"
    formatted_board = [column_labels]
    formatted_board.append(" +-----------------+")

    for i, row in enumerate(board):
        formatted_board.append(f"{8 - i}| {' '.join(row)} |")

    formatted_board.append(" +-----------------+")
    formatted_board.append(column_labels)

    return "\n".join(formatted_board)


def square_to_indices(square):
    column, row = square
    row_index = 8 - int(row)
    col_index = ord(column) - ord("a")
    return row_index, col_index


def validate_pawn_move(board, start_row, start_col, target_row, target_col, color):
    piece = board[start_row][start_col]
    direction = -1 if piece == WHITE_PAWN else 1
    start_row_initial = 6 if piece == WHITE_PAWN else 1

    if target_col == start_col:
        if (
            target_row == start_row + direction
            and board[target_row][target_col] == EMPTY
        ):
            return True
        if (
            target_row == start_row + 2 * direction
            and start_row == start_row_initial
            and board[start_row + direction][start_col] == EMPTY
            and board[target_row][target_col] == EMPTY
        ):
            return True
    elif abs(target_col - start_col) == 1 and target_row == start_row + direction:
        if board[target_row][target_col] != EMPTY and (
            board[target_row][target_col] in BLACK_PIECES
            if color == "w"
            else board[target_row][target_col] in WHITE_PIECES
        ):
            return True

    return False


def validate_knight_move(
    board, start_row, start_col, target_row, target_col, current_color
):
    piece = board[start_row][start_col]
    if current_color == "w" and piece != WHITE_KNIGHT:
        return False
    if current_color == "b" and piece != BLACK_KNIGHT:
        return False

    row_diff = abs(target_row - start_row)
    col_diff = abs(target_col - start_col)

    if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
        target_piece = board[target_row][target_col]
        if (
            target_piece == EMPTY
            or (current_color == "w" and target_piece in BLACK_PIECES)
            or (current_color == "b" and target_piece in WHITE_PIECES)
        ):
            return True
    return False


def validate_bishop_move(
    board, start_row, start_col, target_row, target_col, current_color
):
    # piece = board[start_row][start_col]
    # if current_color == "w" and piece != WHITE_BISHOP:
    #     return False
    # if current_color == "b" and piece != BLACK_BISHOP:
    #     return False

    row_diff = abs(target_row - start_row)
    col_diff = abs(target_col - start_col)
    if row_diff != col_diff:
        return False

    row_step = 1 if target_row > start_row else -1
    col_step = 1 if target_col > start_col else -1
    for step in range(1, row_diff):
        if board[start_row + step * row_step][start_col + step * col_step] != EMPTY:
            return False

    target_piece = board[target_row][target_col]
    if (
        target_piece == EMPTY
        or (current_color == "w" and target_piece in BLACK_PIECES)
        or (current_color == "b" and target_piece in WHITE_PIECES)
    ):
        return True
    return False


def validate_rook_move(
    board, start_row, start_col, target_row, target_col, current_color
):
    # piece = board[start_row][start_col]
    # if current_color == "w" and piece != WHITE_ROOK:
    #     return False
    # if current_color == "b" and piece != BLACK_ROOK:
    #     return False

    if start_row != target_row and start_col != target_col:
        return False

    if start_row == target_row:
        step = 1 if target_col > start_col else -1
        for col in range(start_col + step, target_col, step):
            if board[start_row][col] != EMPTY:
                return False
    else:
        step = 1 if target_row > start_row else -1
        for row in range(start_row + step, target_row, step):
            if board[row][start_col] != EMPTY:
                return False

    target_piece = board[target_row][target_col]
    if (
        target_piece == EMPTY
        or (current_color == "w" and target_piece in BLACK_PIECES)
        or (current_color == "b" and target_piece in WHITE_PIECES)
    ):
        return True
    return False


def validate_queen_move(
    board, start_row, start_col, target_row, target_col, current_color
):
    piece = board[start_row][start_col]
    if current_color == "w" and piece != WHITE_QUEEN:
        return False
    if current_color == "b" and piece != BLACK_QUEEN:
        return False

    if validate_bishop_move(
        board, start_row, start_col, target_row, target_col, current_color
    ) or validate_rook_move(
        board, start_row, start_col, target_row, target_col, current_color
    ):
        return True
    return False


def validate_king_move(
    board, start_row, start_col, target_row, target_col, current_color
):
    piece = board[start_row][start_col]
    if current_color == "w" and piece != WHITE_KING:
        return False
    if current_color == "b" and piece != BLACK_KING:
        return False

    row_diff = abs(target_row - start_row)
    col_diff = abs(target_col - start_col)
    if row_diff <= 1 and col_diff <= 1:
        target_piece = board[target_row][target_col]
        if (
            target_piece == EMPTY
            or (current_color == "w" and target_piece in BLACK_PIECES)
            or (current_color == "b" and target_piece in WHITE_PIECES)
        ):
            return True
    return False


def validate_move(fen, start, target, color):
    board = decode_fen(fen)
    start_row, start_col = square_to_indices(start)
    target_row, target_col = square_to_indices(target)
    piece = board[start_row][start_col]

    if piece == EMPTY:
        return False

    if (color == "w" and piece in BLACK_PIECES) or (
        color == "b" and piece in WHITE_PIECES
    ):
        return False

    if piece in [WHITE_PAWN, BLACK_PAWN]:
        return validate_pawn_move(
            board, start_row, start_col, target_row, target_col, color
        )

    if piece in [WHITE_KNIGHT, BLACK_KNIGHT]:
        return validate_knight_move(
            board, start_row, start_col, target_row, target_col, color
        )

    if piece in [WHITE_BISHOP, BLACK_BISHOP]:
        return validate_bishop_move(
            board, start_row, start_col, target_row, target_col, color
        )

    if piece in [WHITE_ROOK, BLACK_ROOK]:
        return validate_rook_move(
            board, start_row, start_col, target_row, target_col, color
        )

    if piece in [WHITE_QUEEN, BLACK_QUEEN]:
        return validate_queen_move(
            board, start_row, start_col, target_row, target_col, color
        )

    if piece in [WHITE_KING, BLACK_KING]:
        return validate_king_move(
            board, start_row, start_col, target_row, target_col, color
        )

    # Add more piece validation logic here.

    return False
