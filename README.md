# Slide puzzle

React application that allows the user to solve a 15 puzzle. 

Future plans involve finishing a Python server that can receive board states and provide the
front-end a set of moves to solve it. The goal is to train a neural network model with
reinforcement learning so it can solve the puzzle.

Currently a representation of the board along with some utility functions have been written in
Python and the puzzle can be played and solved via the CLI.

How to run locally:

* Run client Node server in one terminal:
```
yarn run dev
```
* Then run the Flask server program in another terminal:
```
cd server
python3 main.py
```
