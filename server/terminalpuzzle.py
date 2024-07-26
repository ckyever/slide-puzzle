import getch
import os
import slidepuzzle
import time

def main():
    size = input("What size would you like the puzzle to be?\n")
    computerSolve = input("Would you like me to solve it?\n")

    puzzle = slidepuzzle.Board(int(size))
    puzzle.scramble()
    updateBoard(puzzle)
    startTime = time.time()

    if inputIsYes(computerSolve):
        puzzle.solve(0.1)
        solveFinished(startTime, puzzle)
    else:
        while True:
            if puzzle.isSolved():
                solveFinished(startTime, puzzle)
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

        
        showReplay = input("\nDo you want to replay your solve?\n")

        if inputIsYes(showReplay):
            puzzle.replayMoves()
        print("Done")

def inputIsYes(input):
    return input.casefold() == "yes".casefold() or input.casefold() == "y".casefold()

def get_key():
    first_char = getch.getch()
    if first_char == '\x1b':
        return {'[A': 'up', '[B': 'down', '[C': 'right', '[D': 'left'}[getch.getch() + getch.getch()]
    else:
        return first_char

def updateBoard(puzzle):
    os.system('cls' if os.name == 'nt' else 'clear')
    puzzle.printCurrentBoard()

def solveFinished(startTime, puzzle):
    endTime = time.time()
    seconds = round(endTime-startTime, 2)
    print("Solved it!")
    print(f"It took {seconds} seconds and {puzzle.getNumberOfMoves()} moves")


if __name__ == "__main__":
    main()