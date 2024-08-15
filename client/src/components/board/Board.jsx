import { useEffect, useState } from 'react';
import Overlay from '../overlay/Overlay';
import Tile from '../tile/Tile';
import Winner from '../winner/Winner';
import NewGame from '../new-game/NewGame';
import './Board.css';

const Board = () => {

    // CKYTODO: Fix the below function as it can sometimes give a unsolvable puzzle state (search web for correct way to shuffle)
    const shuffle = () => 
        new Array(16)
            .fill()
            .map((_, i) => i + 1)
            .sort(() => Math.random() - 0.5)
            .map((x, i) => ({value: x, index: i}));

    const [numbers, setNumbers] = useState(shuffle());

    const moveTile = tile => {
        const blankTileIndex = numbers.find(n => n.value === 16).index;

        // CKYTODO: This is fixed but refactor this in a more explicit way
        const validMoveTilesIndex = [blankTileIndex-4, blankTileIndex+4]

        // Only allow movement of the adjacent tiles if they are not on the next row
        if ((blankTileIndex) % 4 != 0) {
            validMoveTilesIndex.push(blankTileIndex-1)
        }
        if ((blankTileIndex+1) % 4 != 0) {
            validMoveTilesIndex.push(blankTileIndex+1)
        }

        if (!validMoveTilesIndex.includes(tile.index)) {
            return
        }

        const newNumbers = [...numbers].map(number => {
            if (number.index !== blankTileIndex && number.index !== tile.index) {
                return number
            } else if (number.value === 16) {
                return {value: 16, index:tile.index}
            }

            return {value: tile.value, index:blankTileIndex}
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
            <Overlay />
            {numbers.map((x, i) =>
                <Tile key={i} number={x} moveTile={moveTile}/>
            )}
        </div>
        <Winner numbers={numbers} reset={reset}/>
        <NewGame reset={reset}/>
    </div>
}

export default Board