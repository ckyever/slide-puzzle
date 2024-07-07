import unittest
import slidepuzzle

class TestIsValid(unittest.TestCase):
    def test_correct3x3Board(self):
        puzzle = slidepuzzle.Board(3)
        self.assertTrue(puzzle.isValid())

    def test_incorrect3x3Board(self):
        puzzle = slidepuzzle.Board(3)
        puzzle.board[-1][-1] = 9
        self.assertFalse(puzzle.isValid())

if __name__ == '__main__':
    unittest.main()