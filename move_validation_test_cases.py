WHITE_PAWN_TEST_CASES = [
    {
        "fen": "8/8/8/8/8/8/P7/8",
        "expected_moves": [("a2", "a3"), ("a2", "a4")],
        "current_color": "w",
    },
    {"fen": "8/8/8/8/8/P7/8/8", "expected_moves": [("a3", "a4")], "current_color": "w"},
    {
        "fen": "8/8/8/8/1p6/P7/8/8",
        "expected_moves": [("a3", "a4"), ("a3", "b4")],
        "current_color": "w",
    },
    {
        "fen": "8/8/8/8/8/P7/P7/8",
        "expected_moves": [("a3", "a4")],
        "current_color": "w",
    },
    {
        "fen": "8/8/8/8/P7/8/P7/8",
        "expected_moves": [("a2", "a3"), ("a4", "a5")],
        "current_color": "w",
    },
    {
        "fen": "8/8/8/8/8/1p6/P7/8",
        "expected_moves": [("a2", "b3"), ("a2", "a3"), ("a2", "a4")],
        "current_color": "w",
    },
    {
        "fen": "8/8/8/8/8/p1p5/1P6/8",
        "expected_moves": [("b2", "a3"), ("b2", "c3"), ("b2", "b3"), ("b2", "b4")],
        "current_color": "w",
    },
    {"fen": "8/8/8/8/8/1p6/1P6/8", "expected_moves": [], "current_color": "w"},
]

BLACK_PAWN_TEST_CASES = [
    {
        "fen": "8/p7/8/8/8/8/8/8",
        "expected_moves": [("a7", "a6"), ("a7", "a5")],
        "current_color": "b",
    },
    {"fen": "8/8/p7/8/8/8/8/8", "expected_moves": [("a6", "a5")], "current_color": "b"},
    {
        "fen": "8/8/p7/1P6/8/8/8/8",
        "expected_moves": [("a6", "a5"), ("a6", "b5")],
        "current_color": "b",
    },
    {
        "fen": "8/p7/1P6/1P6/8/8/8/8",
        "expected_moves": [("a7", "a6"), ("a7", "a5"), ("a7", "b6")],
        "current_color": "b",
    },
    {
        "fen": "8/p7/p7/8/8/8/8/8",
        "expected_moves": [("a6", "a5")],
        "current_color": "b",
    },
    {
        "fen": "8/p7/8/p7/8/8/8/8",
        "expected_moves": [("a7", "a6"), ("a5", "a4")],
        "current_color": "b",
    },
    {"fen": "8/1p6/1P6/8/8/8/8/8", "expected_moves": [], "current_color": "b"},
]

WHITE_KNIGHT_TEST_CASES = [
    {
        "fen": "8/8/8/8/8/3N4/8/8",
        "expected_moves": [
            ("d3", "c1"),
            ("d3", "b2"),
            ("d3", "c5"),
            ("d3", "e5"),
            ("d3", "f4"),
            ("d3", "f2"),
            ("d3", "e1"),
            ("d3", "b4"),
        ],
        "current_color": "w",
    },
    {
        "fen": "8/8/8/2p1p3/1p3p2/3N4/1p3p2/2p1p3",
        "expected_moves": [
            ("d3", "c1"),
            ("d3", "b2"),
            ("d3", "c5"),
            ("d3", "e5"),
            ("d3", "f4"),
            ("d3", "f2"),
            ("d3", "e1"),
            ("d3", "b4"),
        ],
        "current_color": "w",
    },
    {
        "fen": "8/8/8/8/8/8/8/N7",
        "expected_moves": [("a1", "b3"), ("a1", "c2")],
        "current_color": "w",
    },
    {
        "fen": "8/8/8/2P1P3/1P3P2/3N4/1P3P2/2P1P3",
        "expected_moves": [
            # Only pawn moves valid
            ("b2", "b3"),
            ("f4", "f5"),
            ("c5", "c6"),
            ("b4", "b5"),
            ("c1", "c2"),
            ("e5", "e6"),
            ("f2", "f3"),
            ("e1", "e2"),
        ],
        "current_color": "w",
    },
]

test_cases = WHITE_PAWN_TEST_CASES + BLACK_PAWN_TEST_CASES + WHITE_KNIGHT_TEST_CASES
