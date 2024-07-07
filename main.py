import slidePuzzle

def main():
    puzzle = slidePuzzle.Board(3)
    puzzle.board[-1][-1] = puzzle.board[-1][-2]
    puzzle.board[-1][-2]
    puzzle.print()
    if puzzle.isSolved():
        print('This puzzle is solved')
    else:
        print('This puzzle is NOT solved')

if __name__ == "__main__":
    main()