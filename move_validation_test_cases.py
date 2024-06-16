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


BLACK_KNIGHT_TEST_CASES = [
    {
        "fen": "8/8/8/8/8/3n4/8/8",
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
        "current_color": "b",
    },
    {
        "fen": "8/8/8/2P1P3/1P3P2/3n4/1P3P2/2P1P3",
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
        "current_color": "b",
    },
    {
        "fen": "8/8/8/8/8/8/8/n7",
        "expected_moves": [("a1", "b3"), ("a1", "c2")],
        "current_color": "b",
    },
    {
        "fen": "8/8/8/2p1p3/1p3p2/3n4/1p3p2/2p1p3",
        "expected_moves": [
            # Only pawn moves valid
            ("e5", "e4"),
            ("f2", "f1"),
            ("b4", "b3"),
            ("f4", "f3"),
            ("b2", "b1"),
            ("c5", "c4"),
        ],
        "current_color": "b",
    },
]

WHITE_BISHOP_TEST_CASES = [
    {
        "fen": "8/8/8/8/3B4/8/8/8",
        "expected_moves": [
            ("d4", "a1"),
            ("d4", "b2"),
            ("d4", "c3"),
            ("d4", "e5"),
            ("d4", "f6"),
            ("d4", "g7"),
            ("d4", "h8"),
            ("d4", "g1"),
            ("d4", "f2"),
            ("d4", "e3"),
            ("d4", "c5"),
            ("d4", "b6"),
            ("d4", "a7"),
        ],
        "current_color": "w",
    },
    {
        "fen": "8/8/8/2P1P3/3B4/2P1P3/8/8",
        "expected_moves": [
            # Only pawn moves expected
            ("c3", "c4"),
            ("e3", "e4"),
            ("c5", "c6"),
            ("e5", "e6"),
        ],
        "current_color": "w",
    },
    {
        "fen": "8/8/8/2p1p3/3B4/2p1p3/8/8",
        "expected_moves": [
            ("d4", "c3"),
            ("d4", "e5"),
            ("d4", "e3"),
            ("d4", "c5"),
        ],
        "current_color": "w",
    },
]

BLACK_BISHOP_TEST_CASES = [
    {
        "fen": "8/8/8/8/3b4/8/8/8",
        "expected_moves": [
            ("d4", "a1"),
            ("d4", "b2"),
            ("d4", "c3"),
            ("d4", "e5"),
            ("d4", "f6"),
            ("d4", "g7"),
            ("d4", "h8"),
            ("d4", "g1"),
            ("d4", "f2"),
            ("d4", "e3"),
            ("d4", "c5"),
            ("d4", "b6"),
            ("d4", "a7"),
        ],
        "current_color": "b",
    },
    {
        "fen": "8/8/8/2p1p3/3b4/2p1p3/8/8",
        "expected_moves": [
            # Only pawn moves expected
            ("c3", "c2"),
            ("e3", "e2"),
            ("c5", "c4"),
            ("e5", "e4"),
        ],
        "current_color": "b",
    },
    {
        "fen": "8/8/8/2P1P3/3b4/2P1P3/8/8",
        "expected_moves": [
            ("d4", "c3"),
            ("d4", "e5"),
            ("d4", "e3"),
            ("d4", "c5"),
        ],
        "current_color": "b",
    },
]

WHITE_ROOK_TEST_CASES = [
    {
        "fen": "8/8/8/8/3R4/8/8/8",
        "expected_moves": [
            ("d4", "d1"),
            ("d4", "d2"),
            ("d4", "d3"),
            ("d4", "d5"),
            ("d4", "d6"),
            ("d4", "d7"),
            ("d4", "d8"),
            ("d4", "a4"),
            ("d4", "b4"),
            ("d4", "c4"),
            ("d4", "e4"),
            ("d4", "f4"),
            ("d4", "g4"),
            ("d4", "h4"),
        ],
        "current_color": "w",
    },
    {
        "fen": "8/8/8/3p4/2pRp3/3p4/8/8",
        "expected_moves": [
            ("d4", "d3"),
            ("d4", "d5"),
            ("d4", "c4"),
            ("d4", "e4"),
        ],
        "current_color": "w",
    },
    {
        "fen": "8/8/8/3P4/2PRP3/3P4/8/8",
        "expected_moves": [
            ("c4", "c5"),
            ("e4", "e5"),
            ("d5", "d6"),
        ],
        "current_color": "w",
    },
]

BLACK_ROOK_TEST_CASES = [
    {
        "fen": "8/8/8/8/3r4/8/8/8",
        "expected_moves": [
            ("d4", "d1"),
            ("d4", "d2"),
            ("d4", "d3"),
            ("d4", "d5"),
            ("d4", "d6"),
            ("d4", "d7"),
            ("d4", "d8"),
            ("d4", "a4"),
            ("d4", "b4"),
            ("d4", "c4"),
            ("d4", "e4"),
            ("d4", "f4"),
            ("d4", "g4"),
            ("d4", "h4"),
        ],
        "current_color": "b",
    },
    {
        "fen": "8/8/8/3P4/2PrP3/3P4/8/8",
        "expected_moves": [
            ("d4", "d3"),
            ("d4", "d5"),
            ("d4", "c4"),
            ("d4", "e4"),
        ],
        "current_color": "b",
    },
    {
        "fen": "8/8/8/3p4/2prp3/3p4/8/8",
        "expected_moves": [
            ("e4", "e3"),
            ("d3", "d2"),
            ("c4", "c3"),
        ],
        "current_color": "b",
    },
]

WHITE_QUEEN_TEST_CASES = [
    {
        "fen": "8/8/8/8/3Q4/8/8/8",
        "expected_moves": [
            ("d4", "a1"),
            ("d4", "b2"),
            ("d4", "c3"),
            ("d4", "e5"),
            ("d4", "f6"),
            ("d4", "g7"),
            ("d4", "h8"),
            ("d4", "g1"),
            ("d4", "f2"),
            ("d4", "e3"),
            ("d4", "c5"),
            ("d4", "b6"),
            ("d4", "a7"),
            ("d4", "d1"),
            ("d4", "d2"),
            ("d4", "d3"),
            ("d4", "d5"),
            ("d4", "d6"),
            ("d4", "d7"),
            ("d4", "d8"),
            ("d4", "a4"),
            ("d4", "b4"),
            ("d4", "c4"),
            ("d4", "e4"),
            ("d4", "f4"),
            ("d4", "g4"),
            ("d4", "h4"),
        ],
        "current_color": "w",
    },
    {
        "fen": "8/8/8/2ppp3/2pQp3/2ppp3/8/8",
        "expected_moves": [
            ("d4", "c3"),
            ("d4", "e5"),
            ("d4", "e3"),
            ("d4", "c5"),
            ("d4", "d3"),
            ("d4", "d5"),
            ("d4", "c4"),
            ("d4", "e4"),
        ],
        "current_color": "w",
    },
    {
        "fen": "8/8/8/2PPP3/2PQP3/2PPP3/8/8",
        "expected_moves": [
            ("c5", "c6"),
            ("d5", "d6"),
            ("e5", "e6"),
        ],
        "current_color": "w",
    },
]

BLACK_QUEEN_TEST_CASES = [
    {
        "fen": "8/8/8/8/3q4/8/8/8",
        "expected_moves": [
            ("d4", "a1"),
            ("d4", "b2"),
            ("d4", "c3"),
            ("d4", "e5"),
            ("d4", "f6"),
            ("d4", "g7"),
            ("d4", "h8"),
            ("d4", "g1"),
            ("d4", "f2"),
            ("d4", "e3"),
            ("d4", "c5"),
            ("d4", "b6"),
            ("d4", "a7"),
            ("d4", "d1"),
            ("d4", "d2"),
            ("d4", "d3"),
            ("d4", "d5"),
            ("d4", "d6"),
            ("d4", "d7"),
            ("d4", "d8"),
            ("d4", "a4"),
            ("d4", "b4"),
            ("d4", "c4"),
            ("d4", "e4"),
            ("d4", "f4"),
            ("d4", "g4"),
            ("d4", "h4"),
        ],
        "current_color": "b",
    },
    {
        "fen": "8/8/8/2PPP3/2PqP3/2PPP3/8/8",
        "expected_moves": [
            ("d4", "c3"),
            ("d4", "e5"),
            ("d4", "e3"),
            ("d4", "c5"),
            ("d4", "d3"),
            ("d4", "d5"),
            ("d4", "c4"),
            ("d4", "e4"),
        ],
        "current_color": "b",
    },
    {
        "fen": "8/8/8/2ppp3/2pqp3/2ppp3/8/8",
        "expected_moves": [
            ("e3", "e2"),
            ("d3", "d2"),
            ("c3", "c2"),
        ],
        "current_color": "b",
    },
]

test_cases = (
    WHITE_PAWN_TEST_CASES
    + BLACK_PAWN_TEST_CASES
    + WHITE_KNIGHT_TEST_CASES
    + BLACK_KNIGHT_TEST_CASES
    + WHITE_BISHOP_TEST_CASES
    + BLACK_BISHOP_TEST_CASES
    + WHITE_ROOK_TEST_CASES
    + BLACK_ROOK_TEST_CASES
    + WHITE_QUEEN_TEST_CASES
    + BLACK_QUEEN_TEST_CASES
)
