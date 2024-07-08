import unittest
import slidepuzzle

class Test3x3Board(unittest.TestCase):
    def setUp(self):
        self.puzzle = slidepuzzle.Board(3)

    def test_correctBoard(self):
        self.assertTrue(self.puzzle.isValid())

    def test_incorrectBoard(self):
        self.puzzle.board[-1][-1] = 9
        self.assertFalse(self.puzzle.isValid())

    def test_solvedBoard(self):
        self.assertTrue(self.puzzle.isSolved())

    def test_unsolvedBoard(self):
        self.puzzle.board[-1][-2] = None
        self.puzzle.board[-1][-1] = 8
        self.assertFalse(self.puzzle.isSolved())

class Test4x4Board(unittest.TestCase):
    def setUp(self):
        self.puzzle = slidepuzzle.Board(4)

    def test_correctBoard(self):
        self.assertTrue(self.puzzle.isValid())

    def test_incorrectBoard(self):
        self.puzzle.board[-1][-1] = 15
        self.assertFalse(self.puzzle.isValid())

    def test_solvedBoard(self):
        self.assertTrue(self.puzzle.isSolved())

    def test_unsolvedBoard(self):
        self.puzzle.board[-1][-2] = None
        self.puzzle.board[-1][-1] = 15
        self.assertFalse(self.puzzle.isSolved())

if __name__ == '__main__':
    unittest.main()