import { useState, useEffect} from 'react';
import './App.css';
import axios from 'axios';
import Puzzle from './components/puzzle/Puzzle';

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

  return (
    <div className="container">
      <Puzzle board={puzzle} size={size}/>
      <div className={`result ${solved ? 'show' : ''}`}>You solved it!</div>
    </div>
  )
};

export default App;