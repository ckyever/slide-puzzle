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
        self.puzzle.board[-1][-2] = 0
        self.puzzle.board[-1][-1] = 8
        self.assertFalse(self.puzzle.isSolved())

class Test3x3CornerMoves(unittest.TestCase):
    def setUp(self):
        self.puzzle = slidepuzzle.Board(3)

    def test_moveOptionUp(self):
        self.assertFalse(self.puzzle.slideUp())

    def test_moveOptionRight(self):
        self.puzzle.slideRight()
        correctAfterState = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 0, 8]
        ]
        self.assertTrue(self.puzzle.board == correctAfterState)

    def test_moveOptionDown(self):
        self.puzzle.slideDown()
        correctAfterState = [
            [1, 2, 3],
            [4, 5, 0],
            [7, 8, 6]
        ]
        self.assertTrue(self.puzzle.board == correctAfterState)

    def test_moveOptionLeft(self):
        self.assertFalse(self.puzzle.slideLeft())

class Test3x3CenterMoves(unittest.TestCase):
    def setUp(self):
        self.puzzle = slidepuzzle.Board(3)
        self.puzzle.board = [
            [1, 2, 3],
            [4, 0, 5],
            [7, 8, 6]
        ]
        self.puzzle.emptySquareXindex = 1
        self.puzzle.emptySquareYindex = 1

    def test_moveOptionUp(self):
        self.puzzle.slideUp()
        correctAfterState = [
            [1, 2, 3],
            [4, 8, 5],
            [7, 0, 6]
        ]
        self.assertTrue(self.puzzle.board == correctAfterState)

    def test_moveOptionRight(self):
        self.puzzle.slideRight()
        correctAfterState = [
            [1, 2, 3],
            [0, 4, 5],
            [7, 8, 6]
        ]
        self.assertTrue(self.puzzle.board == correctAfterState)

    def test_moveOptionDown(self):
        self.puzzle.slideDown()
        correctAfterState = [
            [1, 0, 3],
            [4, 2, 5],
            [7, 8, 6]
        ]
        self.assertTrue(self.puzzle.board == correctAfterState)

    def test_moveOptionLeft(self):
        self.puzzle.slideLeft()
        correctAfterState = [
            [1, 2, 3],
            [4, 5, 0],
            [7, 8, 6]
        ]
        self.assertTrue(self.puzzle.board == correctAfterState)

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
        self.puzzle.board[-1][-2] = 0
        self.puzzle.board[-1][-1] = 15
        self.assertFalse(self.puzzle.isSolved())

if __name__ == '__main__':
    unittest.main()