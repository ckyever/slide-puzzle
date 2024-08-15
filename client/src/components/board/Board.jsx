import { useEffect, useState } from 'react';
import Overlay from '../overlay/Overlay';
import Tile from '../tile/Tile';
import Winner from '../winner/Winner';
import NewGame from '../new-game/NewGame';
import './Board.css';

const Board = () => {
    const boardSize = 4; // Number of columns/rows
    const numberOfTiles = 16; 

    // CKYTODO: Fix the below function as it can sometimes give a unsolvable puzzle state (search web for correct way to shuffle)
    const shuffle = () => 
        new Array(numberOfTiles)
            .fill()
            .map((_, i) => i + 1)
            .sort(() => Math.random() - 0.5)
            .map((x, i) => ({value: x, index: i}));

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