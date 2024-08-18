import NewGame from '../new-game/NewGame'
import './Winner.css'

const Winner = ({numbers}) => {
    let message = "You solved it!";

    if (!numbers.every(n => n.value === n.index + 1)) {
        message = "";
    }

    return <div className='winner'>
        <p>{message}</p>
    </div>
}

export default Winner