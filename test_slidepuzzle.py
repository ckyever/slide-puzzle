import unittest
import slidepuzzle

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.puzzle = slidepuzzle.Board(3)

    def test_correct3x3Board(self):
        self.assertTrue(self.puzzle.isValid())

    def test_incorrect3x3Board(self):
        self.puzzle.board[-1][-1] = 9
        self.assertFalse(self.puzzle.isValid())

    def test_solved3x3Board(self):
        self.assertTrue(self.puzzle.isSolved())

    def test_unsolved3x3Board(self):
        self.puzzle.board[-1][-2] = None
        self.puzzle.board[-1][-1] = 8
        self.assertFalse(self.puzzle.isSolved())

if __name__ == '__main__':
    unittest.main()