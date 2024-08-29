import copy
import math
import numpy as np
import os
import random
import time

class Board:
    SLIDE_UP    = "U"
    SLIDE_RIGHT = "R"
    SLIDE_DOWN  = "D"
    SLIDE_LEFT  = "L"

    def __init__(self, size):
        number = 0
        self.size = size
        self.board = [[number := number+1 for _ in range(size)] for _ in range(size)]
        # 0 represents the empty square
        self.board[-1][-1] = 0
        self.initialBoard = copy.deepcopy(self.board)
        self.emptySquareXindex = size-1
        self.emptySquareYindex = size-1
        self.moveHistory = []

    def getSize(self):
        return self.size

    def getBoard(self):
        return self.board

    def setBoard(self, boardArray):
        self.board = boardArray

    def getMoveHistory(self):
        return self.moveHistory

    def getNumberOfMoves(self):
        return len(self.moveHistory)

    def resetBoard(self):
        self.board = copy.deepcopy(self.initialBoard)
        self.moveHistory = []

        for row in range(self.size):
            for column in range(self.size):
                if self.board[row][column] == 0:
                    self.emptySquareYindex = row
                    self.emptySquareXindex = column

    def printBoard(self, board):
        boardString = ""
        for row in board:
            boardString += '['
            for number in row:
                if number == 0:
                    square = " "
                else:
                    square = str(number)
                squareWidth = len(str(self.getNumberOfSquares())) + 2
                boardString += square.center(squareWidth)
            boardString += "]\n"
        print(boardString)

    def printCurrentBoard(self):
        self.printBoard(self.board)

    def clearThenPrintCurrentBoard(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.printCurrentBoard()

    def printInitialBoard(self):
        self.printBoard(self.initialBoard)

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

    def slideUp(self, trackMove=True):
        if self.canSlideUp():
            # Swap empty square with the square below it
            self.swapSquares(
                (self.emptySquareXindex, self.emptySquareYindex), 
                (self.emptySquareXindex, self.emptySquareYindex + 1)
            )
            if trackMove:
                self.moveHistory.append(self.SLIDE_UP)
            return True
        else:
            return False

    def canSlideUp(self):
        # Can slide up if empty square is not on the last row
        return self.emptySquareYindex < (self.size - 1)

    def slideRight(self, trackMove=True):
        if self.canSlideRight():
            # Swap empty square with the square to the left of it
            self.swapSquares(
                (self.emptySquareXindex, self.emptySquareYindex),
                (self.emptySquareXindex - 1, self.emptySquareYindex)
            )
            if trackMove:
                self.moveHistory.append(self.SLIDE_RIGHT)
            return True
        else:
            return False

    def canSlideRight(self):
        # Can slide right if empty square is not on the first column
        return self.emptySquareXindex > 0

    def slideDown(self, trackMove=True):
        if self.canSlideDown():
            # Swap empty square with the square above it
            self.swapSquares(
                (self.emptySquareXindex, self.emptySquareYindex),
                (self.emptySquareXindex, self.emptySquareYindex - 1)
            )
            if trackMove:
                self.moveHistory.append(self.SLIDE_DOWN)
            return True
        else:
            return False

    def canSlideDown(self):
        # Can slide down if empty square is not on the first row
        return self.emptySquareYindex > 0

    def slideLeft(self, trackMove=True):
        if self.canSlideLeft():
            # Swap empty square with the square to the right of it
            self.swapSquares(
                (self.emptySquareXindex, self.emptySquareYindex),
                (self.emptySquareXindex + 1, self.emptySquareYindex)
            )
            if trackMove:
                self.moveHistory.append(self.SLIDE_LEFT)
            return True
        else:
            return False

    def canSlideLeft(self):
        # Can slide left if empty square is not on the last column
        return self.emptySquareXindex < (self.size - 1)

    def scramble(self, minimumNumberOfMoves=100):
        movesRemaining = minimumNumberOfMoves
        movesMade = 0

        while (movesRemaining > 0):
            moveChoice = random.randint(1,4)
            if moveChoice == 1:
                self.slideUp(False)
            elif moveChoice == 2:
                self.slideRight(False)
            elif moveChoice == 3:
                self.slideDown(False)
            elif moveChoice == 4:
                self.slideLeft(False)

            movesMade += 1
            movesRemaining -= 1

            if (movesRemaining == 0 and self.isSolved()):
                movesRemaining = 100

        self.initialBoard = copy.deepcopy(self.board)

    def makeMoves(self, moveList, printBoard=True, secondsBetweenMoves=0.5):
        for move in moveList:
            if (move == self.SLIDE_UP):
                self.slideUp()
            elif (move == self.SLIDE_RIGHT):
                self.slideRight()
            elif (move == self.SLIDE_DOWN):
                self.slideDown()
            elif (move == self.SLIDE_LEFT):
                self.slideLeft()
            else:
                raise Exception(f"Invalid move: {move}")

            if printBoard:
                self.clearThenPrintCurrentBoard()
                time.sleep(secondsBetweenMoves)
    
    def replayMoves(self):
        moveList = self.getMoveHistory()
        self.resetBoard()
        self.makeMoves(moveList)

    def solve(self, secondsBetweenMoves=0.25):
        moveOptions = [self.SLIDE_UP, self.SLIDE_RIGHT, self.SLIDE_DOWN, self.SLIDE_LEFT]
        while not self.isSolved():
            move = random.choice(moveOptions)
            if move == self.SLIDE_UP:
                self.slideUp()
            elif move == self.SLIDE_RIGHT:
                self.slideRight()
            elif move == self.SLIDE_DOWN:
                self.slideDown()
            elif move == self.SLIDE_LEFT:
                self.slideLeft()

            self.clearThenPrintCurrentBoard()
            time.sleep(secondsBetweenMoves)