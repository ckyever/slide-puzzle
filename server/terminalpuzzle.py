import getch
import os
import slidepuzzle
import time

def main():
    size = input("What size would you like the puzzle to be?\n")

    puzzle = slidepuzzle.Board(int(size))
    puzzle.scramble()
    updateBoard(puzzle)

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
                updateBoard(puzzle)
        elif key == 'right':
            if puzzle.slideRight():
                updateBoard(puzzle)
        elif key == 'down':
            if puzzle.slideDown():
                updateBoard(puzzle)
        elif key == 'left':
            if puzzle.slideLeft():
                updateBoard(puzzle)

def get_key():
    first_char = getch.getch()
    if first_char == '\x1b':
        return {'[A': 'up', '[B': 'down', '[C': 'right', '[D': 'left'}[getch.getch() + getch.getch()]
    else:
        return first_char

def updateBoard(puzzle):
    os.system('cls' if os.name == 'nt' else 'clear')
    puzzle.printCurrentBoard()

if __name__ == "__main__":
    main()