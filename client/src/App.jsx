import { useState, useEffect} from 'react';
import './App.css';
import Board from './components/board/Board';
import axios from 'axios';

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
    <div className="App">
      <Board />
    </div>
  )
};

export default App;