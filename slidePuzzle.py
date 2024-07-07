import math
import numpy

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
        print(numpy.matrix(self.board))

    def isSquareBlank(self, index):
        return math.pow(self.size, 2)

    def isSolved(self):
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