import { useState, useEffect} from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import axios from 'axios'

function App() {
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
      <div>
        <p>
          {puzzle.map((row, rowIndex) => (
            <div key={rowIndex}>
              {row.map((tile, tileIndex) => (
                <span>[{tile}]</span>
              ))}
              <br></br>
            </div>
          ))}
        </p>
      </div>
    </>
  )
}

export default App
