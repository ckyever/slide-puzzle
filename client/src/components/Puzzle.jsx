import './Puzzle.css'

function Puzzle(props) {

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
}

export default Puzzle