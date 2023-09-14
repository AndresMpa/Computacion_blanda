from tic_tac_toe import check_winner, is_full
import unittest


class TestTicTacToe(unittest.TestCase):
    def test_check_winner(self):
        # Prueba de la función check_winner
        board1 = [['X', 'O', 'X'],
                  ['O', 'X', 'O'],
                  ['O', 'X', 'X']]
        self.assertTrue(check_winner(board1, 'X'))  # X debe ganar
        self.assertFalse(check_winner(board1, 'O'))  # O no debe ganar

        board2 = [['X', 'O', ' '],
                  ['O', 'X', 'O'],
                  ['O', 'X', 'X']]
        self.assertTrue(check_winner(board2, 'X'))  # X debe ganar
        self.assertFalse(check_winner(board2, 'O'))  # O no debe ganar

        board3 = [['X', 'O', 'O'],
                  ['O', 'X', 'X'],
                  ['O', 'X', 'O']]
        self.assertFalse(check_winner(board3, 'O'))  # O no debe ganar
        self.assertFalse(check_winner(board3, 'X'))  # X no debe ganar

    def test_is_full(self):
        # Prueba de la función is_full
        board1 = [['X', 'O', 'X'],
                  ['O', 'X', 'O'],
                  ['O', 'X', 'X']]
        self.assertTrue(is_full(board1))  # El tablero está lleno

        board2 = [['X', 'O', ' '],
                  ['O', 'X', 'O'],
                  ['O', 'X', 'X']]
        self.assertFalse(is_full(board2))  # El tablero no está lleno

        board3 = [['X', 'O', 'O'],
                  ['O', 'X', 'X'],
                  ['O', 'X', 'O']]
        self.assertTrue(is_full(board3))  # El tablero está lleno


if __name__ == "__main__":
    unittest.main()
