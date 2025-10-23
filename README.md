# Slide puzzle

React application that allows the user to solve a sliding 15 puzzle.

👉 [Demo](https://ckyever.github.io/slide-puzzle)

Future plans involve finishing a Python server that can receive board states and provide the
front-end a set of moves to solve it.

Currently a representation of the board along with some utility functions have been written in
Python and the puzzle can be played and solved via the CLI.

How to run locally:

- Ensure node, yarn and vite are installed on your machine
- Run client Node server in one terminal:

```
yarn run dev
```

- Then run the Flask server program in another terminal:

```
cd server
python3 main.py
```
