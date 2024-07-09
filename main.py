import slidepuzzle

def main():
    puzzle = slidepuzzle.Board(3)
    puzzle.print()
    puzzle.slideRight()
    puzzle.print()
    puzzle.slideRight()
    puzzle.print()
    puzzle.slideDown()
    puzzle.print()
    puzzle.slideDown()
    puzzle.print()

if __name__ == "__main__":
    main()
