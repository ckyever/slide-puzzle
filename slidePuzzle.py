import numpy

class Board:
    def __init__(self, size):
        number = 0
        self.board = [[number:=number+1 for _ in range(size)] for _ in range(size)]
        self.board[-1][-1] = None

    def print(self):
        print(numpy.matrix(self.board))

