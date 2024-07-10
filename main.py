import getch
import slidepuzzle
import time

def main():

    size = input("What size would you like the puzzle to be?\n")
    print()

    puzzle = slidepuzzle.Board(int(size))
    puzzle.scramble()
    puzzle.print()

    startTime = time.time()

    while True:
        if puzzle.isSolved():
            endTime = time.time()
            seconds = round(endTime-startTime, 2)
            print("You solved it!")
            print(f"It took you {seconds} seconds")
            break

        key = getch.getch()
        if key == 'q':
            break
        elif key == 'w':
            if puzzle.slideUp():
                puzzle.print()
        elif key == 'd':
            if puzzle.slideRight():
                puzzle.print()
        elif key == 's':
            if puzzle.slideDown():
                puzzle.print()
        elif key == 'a':
            if puzzle.slideLeft():
                puzzle.print()

if __name__ == "__main__":
    main()