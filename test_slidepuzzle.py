import unittest
import slidepuzzle

class Test3x3Board(unittest.TestCase):
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

class Test4x4Board(unittest.TestCase):
    def setUp(self):
        self.puzzle = slidepuzzle.Board(4)

    def test_correct4x4Board(self):
        self.assertTrue(self.puzzle.isValid())

    def test_incorrect4x4Board(self):
        self.puzzle.board[-1][-1] = 15
        self.assertFalse(self.puzzle.isValid())

    def test_solved4x4Board(self):
        self.assertTrue(self.puzzle.isSolved())

    def test_unsolved4x4Board(self):
        self.puzzle.board[-1][-2] = None
        self.puzzle.board[-1][-1] = 15
        self.assertFalse(self.puzzle.isSolved())

if __name__ == '__main__':
    unittest.main()