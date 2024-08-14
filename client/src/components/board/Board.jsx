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

    // CKYTODO: Fix scenario where if the blank tile is on the right clicking the left-most tile on the next row will move it illegaly
    const moveTile = tile => {
        const i16 = numbers.find(n => n.value === 16).index;
        if (![i16-1, i16+1, i16-4, i16+4].includes(tile.index))
            return

        const newNumbers = [...numbers].map(number => {
            if (number.index !== i16 && number.index !== tile.index)
                return number
            else if (number.value === 16)
                return {value: 16, index:tile.index}

            return {value: tile.value, index:i16}
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