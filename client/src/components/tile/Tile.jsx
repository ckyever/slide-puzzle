import './Tile.css'

const Tile = ({number, moveTile, numberOfTiles}) =>
    <div 
        onClick={() => moveTile(number)}
        className={`number ${number.value === numberOfTiles ? 'disabled' : ''} slot--${number.index}`}>
        {number.value === numberOfTiles ? '' : number.value}
    </div>

export default Tile