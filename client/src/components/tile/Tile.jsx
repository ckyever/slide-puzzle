import './Tile.css'

const Tile = ({number, moveTile}) =>
    <div 
        onClick={() => moveTile(number)}
        className={`number ${number.value === 16 ? 'disabled' : ''} slot--${number.index}`}>
        {number.value === 16 ? '' : number.value}
    </div>

export default Tile