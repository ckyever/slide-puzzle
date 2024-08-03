import { useState, useEffect} from 'react';
import './App.css';
import axios from 'axios';
import Puzzle from './components/Puzzle';

const App = () => {
  const [count, setCount] = useState(0);
  const [puzzle, setArray] = useState([]);

  const fetchAPI = async () => {
    const response = await axios.get("http://localhost:8080/api/puzzle")
    setArray(response.data.puzzle)
  };

  useEffect(() => {
    fetchAPI()
  }, []);

  return (
    <>
      <Puzzle board={puzzle}/>
    </>
  )
};

export default App;