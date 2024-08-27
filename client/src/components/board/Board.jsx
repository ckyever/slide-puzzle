import axios from 'axios';
import { useEffect, useState } from 'react';

import Action from '../action/Action';
import Overlay from '../overlay/Overlay';
import Tile from '../tile/Tile';
import Winner from '../winner/Winner';

import './Board.css';

const Board = () => {
    const boardSize = 4; // Number of columns/rows
    const numberOfTiles = boardSize*boardSize; 
    const emptyTileValue = numberOfTiles;

    const slideUp = 'U';
    const slideRight = 'R';
    const slideDown = 'D';
    const slideLeft = 'L';

    const createNewPuzzle = () => {
        let puzzle = null;

        puzzle = Array(numberOfTiles)
            .fill()
            .map((_, i) => i + 1)
            .sort(() => Math.random() - 0.5)
            .map((x, i) => ({value: x, index: i}));

        // Always place empty tile in the bottom right corner
        const emptyTileIndex = puzzle.findIndex(tile => tile.value === emptyTileValue);
        puzzle[emptyTileIndex].value = puzzle[numberOfTiles-1].value;
        puzzle[numberOfTiles-1].value = emptyTileValue;

        // When empty tile is in the bottom row and board size is even the permutation parity
        // must be even (see https://www.geeksforgeeks.org/check-instance-15-puzzle-solvable/)
        if (getPermutationParity(puzzle) % 2 != 0) {
            // In the case it is odd let us do one more inversion to make it even
            const tempValue = puzzle[0].value;
            puzzle[0].value = puzzle[1].value;
            puzzle[1].value = tempValue;
        }

        return puzzle;
    }

    const getPermutationParity = (puzzle) => {
        let inversions = 0;
        for (let i = 0; i < puzzle.length - 1; i++) {
            for (let j = i + 1; j < puzzle.length; j++) {
                if (puzzle[j].value != emptyTileValue && puzzle[i].value != emptyTileValue
                    && puzzle[i].value > puzzle[j].value) {
                        inversions++;
                }
            }
        }

        return inversions;
    }

    const [tileArray, setTileArray] = useState(createNewPuzzle());
    const [moves, setMoves] = useState([]);

    const moveTile = tile => {
        const emptySpaceIndex = tileArray.find(n => n.value === emptyTileValue).index;

        const emptySpaceRow = Math.floor(emptySpaceIndex / boardSize);
        const emptySpaceColumn = emptySpaceIndex % boardSize;

        const tileRow = Math.floor(tile.index / boardSize);
        const tileColumn = tile.index % boardSize;

        const isTileAdjacentToEmptySpace =
            ((tileRow == emptySpaceRow && Math.abs(tileColumn - emptySpaceColumn) === 1) || // Same row adjacent column
            (tileColumn == emptySpaceColumn && Math.abs(tileRow - emptySpaceRow) === 1));   // Same column adjacent row

        if (!isTileAdjacentToEmptySpace) {
            return;
        }

        const newTileArray = [...tileArray].map(number => {
            if (number.index !== emptySpaceIndex && number.index !== tile.index) {
                return number;
            } else if (number.value === emptyTileValue) {
                return {value: emptyTileValue, index:tile.index}
            }

            return {value: tile.value, index:emptySpaceIndex}
        });

        setTileArray(newTileArray);
    }

    const animateMoves = async () => {
        for (let move of moves) {
            await new Promise(resolve => {
                setTileArray(prevTileArray => {
                    const emptyTileIndex = prevTileArray.findIndex(tile => tile.value === emptyTileValue);
                    let tileToMoveIndex = null;

                    switch (move) {
                        case slideUp:
                            tileToMoveIndex = prevTileArray.findIndex(tile => tile.index === emptyTileIndex + boardSize);
                            break;
                        case slideRight:
                            tileToMoveIndex = prevTileArray.findIndex(tile => tile.index === emptyTileIndex - 1);
                            break;
                        case slideDown:
                            tileToMoveIndex = prevTileArray.findIndex(tile => tile.index === emptyTileIndex - boardSize);
                            break;
                        case slideLeft:
                            tileToMoveIndex = prevTileArray.findIndex(tile => tile.index === emptyTileIndex + 1);
                            break;
                    }

                    if (tileToMoveIndex === null) {
                        resolve();
                        return prevTileArray;
                    }

                    const newTileArray = [...prevTileArray];

                    const tileToMove = newTileArray[tileToMoveIndex];
                    newTileArray[emptyTileIndex] = { ...tileToMove, index: emptyTileIndex };
                    newTileArray[tileToMoveIndex] = { value: emptyTileValue, index: tileToMoveIndex };

                    resolve();
                    return newTileArray;
                });
            });

            await new Promise((resolve) => setTimeout(resolve, 500)); // Wait before the next move
        }
        setMoves([]);
    };

    // CKYTODO: This doesn't work if you first move the board around manually then click the solve button. It seems to be using the 
    // empty tile index of the initial board state instead of the current one
    const solve = async () => {
        try {
            const response = await axios.post("http://localhost:8080/api/puzzle", tileArray);
            setMoves(response.data.moves);
        } catch (error) {
            console.error('Error receiving moves to solve puzzle:', error);
        }
    }

    const reset = () => {
        setTileArray(createNewPuzzle());
    }

    useEffect(reset, []);

    useEffect(() => {
        if (moves.length > 0) {
            animateMoves();
        }
    }, [moves]);

    return <div className="game">
        <Winner tileArray={tileArray}/>
        <div className="board">
            <Overlay numberOfTiles={numberOfTiles} />
            {tileArray.map((tile, index) =>
                <Tile key={index} number={tile} moveTile={moveTile} numberOfTiles={numberOfTiles}/>
            )}
        </div>
        <div className="actions">
            <Action action={reset} actionText="New Game"/>
            <Action action={solve} actionText="Solve"/>
        </div>
    </div>
}

export default Board