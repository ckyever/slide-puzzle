import math
import numpy as np

# 0 represents the empty square
class Board:
    def __init__(self, size):
        number = 0
        self.size = size
        self.board = [[number := number+1 for _ in range(size)] for _ in range(size)]
        self.board[-1][-1] = 0
        self.emptySquareXindex = size-1
        self.emptySquareYindex = size-1

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
    
    def swapSquares(self, square1, square2):

        # Set where the new empty square is going to be located
        if square1 == (self.emptySquareXindex, self.emptySquareYindex):
            self.emptySquareXindex = square2[0]
            self.emptySquareYindex = square2[1]
        elif square2 == (self.emptySquareXindex, self.emptySquareYindex):
            self.emptySquareXindex = square1[0]
            self.emptySquareYindex = square1[1]
        else:
            raise Exception("Should not be able to swap squares if one of them is not empty")

        temp = self.board[square1[1]][square1[0]]
        self.board[square1[1]][square1[0]] = self.board[square2[1]][square2[0]]
        self.board[square2[1]][square2[0]] = temp

    def slideUp(self):
        if self.canSlideUp():
            # Swap empty square with the square below it
            self.swapSquares(
                (self.emptySquareXindex, self.emptySquareYindex), 
                (self.emptySquareXindex, self.emptySquareYindex + 1)
            )
            return True
        else:
            return False

    def canSlideUp(self):
        # Can slide up if empty square is not on the last row
        return self.emptySquareYindex < (self.size - 1)

    def slideRight(self):
        if self.canSlideRight():
            # Swap empty square with the square to the left of it
            self.swapSquares(
                (self.emptySquareXindex, self.emptySquareYindex),
                (self.emptySquareXindex - 1, self.emptySquareYindex)
            )
            return True
        else:
            return False

    def canSlideRight(self):
        # Can slide right if empty square is not on the first column
        return self.emptySquareXindex > 0

    def slideDown(self):
        if self.canSlideDown():
            # Swap empty square with the square above it
            self.swapSquares(
                (self.emptySquareXindex, self.emptySquareYindex),
                (self.emptySquareXindex, self.emptySquareYindex - 1)
            )
            return True
        else:
            return False

    def canSlideDown(self):
        # Can slide down if empty square is not on the first row
        return self.emptySquareYindex > 0

    def slideLeft(self):
        if self.canSlideLeft():
            # Swap empty square with the square to the right of it
            self.swapSquares(
                (self.emptySquareXindex, self.emptySquareYindex),
                (self.emptySquareXindex + 1, self.emptySquareYindex)
            )
            return True
        else:
            return False

    def canSlideLeft(self):
        # Can slide left if empty square is not on the last column
        return self.emptySquareYindex < (self.size - 1)
