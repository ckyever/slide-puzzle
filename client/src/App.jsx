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

  return (
    <div>
    </div>
  )
};

export default App;