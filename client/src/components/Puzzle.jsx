import PropTypes from 'prop-types';
import './Puzzle.css';

const Puzzle = props => {
  return (
    <div
      className='board'
      style={{gridTemplateColumns: `repeat(${props.size}, 1fr)`}}
    >
        {props.board.map((row) => (
            row.map((tile, tileIndex) => (
              <div key={tileIndex} className='tile'>{tile}</div>
            ))
        ))}
    </div>
  )
};

Puzzle.propTypes = {board: PropTypes.array.isRequired};

export default Puzzle;