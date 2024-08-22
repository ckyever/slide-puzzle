import './Winner.css'
import ConfettiExplosion from 'react-confetti-explosion';

const Winner = ({tileArray}) => {
    let content = ""

    if (tileArray.every(n => n.value === n.index + 1)) {
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