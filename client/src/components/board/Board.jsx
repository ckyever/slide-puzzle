import { useEffect, useState } from 'react';
import Overlay from '../overlay/Overlay';
import Tile from '../tile/Tile';
import Winner from '../winner/Winner';
import NewGame from '../new-game/NewGame';
import './Board.css';

const Board = () => {
    const boardSize = 4; // Number of columns/rows
    const numberOfTiles = boardSize*boardSize; 

    const shuffle = () => {
        let puzzle = Array(numberOfTiles)
            .fill()
            .map((_, i) => i + 1)
            .sort(() => Math.random() - 0.5)
            .map((x, i) => ({value: x, index: i}));

        // If puzzle is not solvable we can assume (parity of permutations + taxicab distance of empty tile)
        // is odd. So if we make one more swap this should bring the total to even
        if (!isSolvable(puzzle)) {
            const index1 = puzzle.indexOf(1);
            const index2 = puzzle.indexOf(2);
            [puzzle[index1], puzzle[index2]] = [puzzle[index2], puzzle[index1]];
        }

        return puzzle;
    };

    const isSolvable = (puzzle) => {
        let inversions = 0;
        puzzle.forEach((value, i) => {
            for (let j = i + 1; j < numberOfTiles; j++) {
                if (value > puzzle[j] && value !== 0 && puzzle[j] !== 0) {
                    inversions++;
                }
            }
        });
        const row = Math.floor(puzzle.indexOf(0) / boardSize) + 1;
        return (inversions + row) % 2 === 0;
    };

    const [numbers, setNumbers] = useState(shuffle());

    const moveTile = tile => {
        const emptySpaceIndex = numbers.find(n => n.value === numberOfTiles).index;

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
                return number
            } else if (number.value === numberOfTiles) {
                return {value: numberOfTiles, index:tile.index}
            }

            return {value: tile.value, index:emptySpaceIndex}
        });

        setNumbers(newNumbers);
    }

    const reset = () => {
        console.log('Reset click');
        setNumbers(shuffle());
    }

    useEffect(reset, [])

    return <div className="game">
        <div className="board">
            <Overlay numberOfTiles={numberOfTiles} />
            {numbers.map((x, i) =>
                <Tile key={i} number={x} moveTile={moveTile} numberOfTiles={numberOfTiles}/>
            )}
        </div>
        <Winner numbers={numbers} reset={reset}/>
        <NewGame reset={reset}/>
    </div>
}

export default Board