import NewGame from '../new-game/NewGame'
import './Winner.css'

const Winner = ({numbers}) => {
    if (!numbers.every(n => n.value === n.index + 1))
        return null;

    return <div 
        className='winner'>
            <p>You solved it!</p>
            <NewGame />
        </div>
}

export default Winner