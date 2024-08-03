import PropTypes from 'prop-types';
import './Puzzle.css';

const Puzzle = props => {

  return (
    <>
      {props.board.map((row, rowIndex) => (
        <div key={rowIndex}>
          {row.map((tile, tileIndex) => (
            <span key={tileIndex}>[{tile}]</span>
          ))}
          <br></br>
        </div>
      ))}
    </>
  )
};

Puzzle.prototype = {board: PropTypes.array.isRequired};

export default Puzzle;