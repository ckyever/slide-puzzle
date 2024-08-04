import { useState, useEffect} from 'react';
import './App.css';
import axios from 'axios';
import Puzzle from './components/puzzle/Puzzle';

const App = () => {
  const [puzzle, setArray] = useState([]);
  const [size, setNumber] = useState(0);

  const fetchAPI = async () => {
    const response = await axios.get("http://localhost:8080/api/puzzle")
    setArray(response.data.puzzle)
    setNumber(response.data.size)
  };

  useEffect(() => {
    fetchAPI()
  }, []);

  return (
    <>
      <Puzzle board={puzzle} size={size}/>
    </>
  )
};

export default App;