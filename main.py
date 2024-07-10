import slidepuzzle

def main():
    puzzle = slidepuzzle.Board(4)
    puzzle.print()
    puzzle.scramble(100)
    puzzle.print()

if __name__ == "__main__":
    main()
