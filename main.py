import slidepuzzle

def main():
    puzzle = slidepuzzle.Board(3)
    puzzle.print()
    if puzzle.isSolved():
        print('This puzzle is solved')
    else:
        print('This puzzle is NOT solved')

    if puzzle.isValid():
        print('This puzzle is valid')
    else:
        print('This puzzle is NOT valid')

if __name__ == "__main__":
    main()
