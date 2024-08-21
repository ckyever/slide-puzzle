import { useEffect, useState } from 'react';
import Overlay from '../overlay/Overlay';
import Tile from '../tile/Tile';
import Winner from '../winner/Winner';
import Action from '../action/Action';
import './Board.css';
import axios from 'axios';

const Board = () => {
    const boardSize = 4; // Number of columns/rows
    const numberOfTiles = boardSize*boardSize; 
    const emptyTileValue = numberOfTiles;

    const slideUp = 'U';
    const slideRight = 'R';
    const slideDown = 'D';
    const slideLeft = 'L';

    const shuffle = () => {
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
    };

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

    const [numbers, setNumbers] = useState(shuffle());

    const moveTile = tile => {
        const emptySpaceIndex = numbers.find(n => n.value === emptyTileValue).index;

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

        const newNumbers = [...numbers].map(number => {
            if (number.index !== emptySpaceIndex && number.index !== tile.index) {
                return number;
            } else if (number.value === emptyTileValue) {
                return {value: emptyTileValue, index:tile.index};
            }

            return {value: tile.value, index:emptySpaceIndex};
        });

        console.log(newNumbers);
        setNumbers(newNumbers);
    }

    const moveByDirection = direction => {
        const emptyTileIndex = numbers.findIndex(tile => tile.value === emptyTileValue);
        let tileToMoveIndex = null;
        switch (direction) {
            case slideUp:
                tileToMoveIndex = numbers.findIndex(tile => tile.index === emptyTileIndex + boardSize);
                break;
            case slideRight:
                tileToMoveIndex = numbers.findIndex(tile => tile.index === emptyTileIndex - 1);
                break;
            case slideDown:
                tileToMoveIndex = numbers.findIndex(tile => tile.index === emptyTileIndex - boardSize);
                break;
            case slideLeft:
                tileToMoveIndex = numbers.findIndex(tile => tile.index === emptyTileIndex + 1);
                break;
        }
        moveTile(numbers[tileToMoveIndex]);
    };

    const moveByDirectionAsync = async (direction) => {
        return new Promise((resolve) => {
            moveByDirection(direction);
            setTimeout(resolve, 0); // Ensure the state has time to update
        });
    };

    const reset = () => {
        setNumbers(shuffle());
    }

    const solve = async () => {
        try {
            const response = await axios.post("http://localhost:8080/api/puzzle", numbers);
            const moves = response.data.moves;

            for (let i=0; i < moves.length; i++) {
                // ckytodo: Board state is not refreshing correctly in between moves
                await moveByDirectionAsync(moves[i]);
                await new Promise(resolve => setTimeout(resolve, 1500));
            }
        } catch (error) {
            console.error('Error solving puzzle:', error);
        }
    }

    useEffect(reset, [])

    return <div className="game">
        <Winner numbers={numbers}/>
        <div className="board">
            <Overlay numberOfTiles={numberOfTiles} />
            {numbers.map((x, i) =>
                <Tile key={i} number={x} moveTile={moveTile} numberOfTiles={numberOfTiles}/>
            )}
        </div>
        <div className="actions">
            <Action action={reset} actionText="New Game"/>
            <Action action={solve} actionText="Solve"/>
        </div>
    </div>
}

export default Board