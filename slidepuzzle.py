import math
import numpy as np

class Board:
    def __init__(self, size):
        number = 0
        self.size = size
        self.board = [[number := number+1 for _ in range(size)] for _ in range(size)]
        self.board[-1][-1] = None

    def getSize(self):
        return self.size

    def getBoard(self):
        return self.board

    def print(self):
        print(np.array(self.board))

    def getNumberOfSquares(self):
        return int(math.pow(self.size, 2))

    def isSquareBlank(self, index):
        return self.getNumberOfSquares() == index

    def isValid(self):
        numbers = np.array(self.board).flatten()

        # Handles sorting for None
        sortedNumbers = sorted(numbers, key=lambda x: (x is None, x))

        expectedNumbers = [number for number in range(1, self.getNumberOfSquares() + 1)]
        expectedNumbers[-1] = None

        return sortedNumbers == expectedNumbers

    def isSolved(self):
        if not self.isValid():
            return False

        expectedNumber = 1

        for row in self.board:
            for number in row:
                if number is None and self.isSquareBlank(expectedNumber):
                    expectedNumber += 1
                elif number == expectedNumber:
                    expectedNumber += 1
                else:
                    return False
        return True