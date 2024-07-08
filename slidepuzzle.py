import math
import numpy as np

# 0 represents the empty square
class Board:
    def __init__(self, size):
        number = 0
        self.size = size
        self.board = [[number := number+1 for _ in range(size)] for _ in range(size)]
        self.board[-1][-1] = 0

    def getSize(self):
        return self.size

    def getBoard(self):
        return self.board

    def print(self):
        prettyBoard = np.array(self.board)
        print() # Add new line
        print(prettyBoard)

    def getNumberOfSquares(self):
        return int(math.pow(self.size, 2))

    def isSquareBlank(self, index):
        return self.getNumberOfSquares() == index

    def isSquareValid(self, index):
        return 1 <= index < self.getNumberOfSquares()

    def isValid(self):
        numbers = np.array(self.board).flatten()

        sortedNumbers = sorted(numbers)

        expectedNumbers = [number for number in range(0, self.getNumberOfSquares())]

        return sortedNumbers == expectedNumbers

    def isSolved(self):
        if not self.isValid():
            return False

        expectedNumber = 1

        for row in self.board:
            for number in row:
                if number == 0 and self.isSquareBlank(expectedNumber):
                    expectedNumber += 1
                elif number == expectedNumber:
                    expectedNumber += 1
                else:
                    return False
        return True

    def move(self, square):
        """
        1. Is square a valid number within the board e.g. 3x3 - between (inclusive) 1 and 8
        2. Is the square chosen moveable - is it adjacent an empty square
        3. Make the move on the board!
        """
        pass