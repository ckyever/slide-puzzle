import slidepuzzle
import keyboard

def main():

    size = input("What size would you like the puzzle to be?\n")
    print()

    puzzle = slidepuzzle.Board(int(size))
    puzzle.print()

if __name__ == "__main__":
    main()
