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

        key = get_key()
        if key == 'q':
            break
        elif key == 'up':
            if puzzle.slideUp():
                puzzle.print()
        elif key == 'right':
            if puzzle.slideRight():
                puzzle.print()
        elif key == 'down':
            if puzzle.slideDown():
                puzzle.print()
        elif key == 'left':
            if puzzle.slideLeft():
                puzzle.print()

def get_key():
    first_char = getch.getch()
    if first_char == '\x1b':
        return {'[A': 'up', '[B': 'down', '[C': 'right', '[D': 'left'}[getch.getch() + getch.getch()]
    else:
        return first_char

if __name__ == "__main__":
    main()