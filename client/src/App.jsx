import { useState, useEffect} from 'react';
import './App.css';
import axios from 'axios';
import Puzzle from './components/puzzle/Puzzle';

// CKYTODO: Change this so user interaction with puzzle occurs on the client side
// CKYTODO: All the python flask server should be going is receiving puzzle states
// CKYTODO: and returning a list of moves that would solve that puzzle state

const App = () => {
  const [puzzle, setArray] = useState([]);
  const [size, setNumber] = useState(0);
  const [solved, setBoolean] = useState(0);

  const fetchPuzzle = async () => {
    const response = await axios.get("http://localhost:8080/api/puzzle");
    setArray(response.data.puzzle);
    setNumber(response.data.size);
    setBoolean(response.data.solved);
  };

  // Initial fetch of board  
  useEffect(() => {
    fetchPuzzle();
  }, []);

  const handleKeyDown = async (event) => {
    let direction = '';
    switch (event.key) {
      case 'ArrowUp':
        direction = 'u';
        break;
      case 'ArrowRight':
        direction = 'r';
        break;
      case 'ArrowDown':
        direction = 'd';
        break;
      case 'ArrowLeft':
        direction = 'l';
        break;
      default:
        return;
    }

    const data = {move: direction};
    const result = await axios.post("http://localhost:8080/api/puzzle", data);
    fetchPuzzle();
  }

  useEffect(() => {
    window.addEventListener('keydown', handleKeyDown);

    return () => {
      window.removeEventListener('keydown', handleKeyDown);
    }
  }, []);

  const handleNewGame = async () => {
    const result = await axios.post("http://localhost:8080/api/puzzle/new", {});
    fetchPuzzle();
  };

  useEffect(() => {
    const newGameButton = document.getElementById("new-game");
    newGameButton.addEventListener("click", handleNewGame);

    return () => {
      newGameButton.removeEventListener("click", newGameButton);
    }
  });

  return (
    <div className="container">
      <Puzzle board={puzzle} size={size}/>
      <div className={`result ${solved ? 'show' : ''}`}>You solved it!</div>
      <button id="new-game" className={`new-game ${solved ? 'show' : ''}`}>New Game</button>
    </div>
  )
};

export default App;