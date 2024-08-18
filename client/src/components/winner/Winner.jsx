import './Winner.css'
import ConfettiExplosion from 'react-confetti-explosion';

const Winner = ({numbers}) => {
    let content = ""

    if (numbers.every(n => n.value === n.index + 1)) {
        content = (
            <>
                <p>You solved it!</p>
                <ConfettiExplosion />
            </>
        );
    }

    return <div className='winner'>{content}</div>
}

export default Winner