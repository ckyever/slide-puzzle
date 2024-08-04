import PropTypes from 'prop-types';
import './Puzzle.css';
import Tile from '../tile/Tile';

const Puzzle = props => {
  return (
    <div
      className='board'
      style={{gridTemplateColumns: `repeat(${props.size}, 1fr)`}}
    >
        {props.board.map((row) => (
            row.map((tileNumber, tileIndex) => (
              <Tile key={tileIndex} tileNumber={tileNumber} />
            ))
        ))}
    </div>
  )
};

Puzzle.propTypes = {board: PropTypes.array.isRequired};

export default Puzzle;