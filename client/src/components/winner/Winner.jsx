import './Winner.css'
import ConfettiExplosion from 'react-confetti-explosion';

const Winner = ({tileArray}) => {
    let content = ""

    if (tileArray.every(n => n.value === n.index + 1)) {
        content = (
            <>
                <p>You solved it!</p>
                <ConfettiExplosion duration={2500} width={2000} force={0.6}/>
            </>
        );
    }

    return <div className='winner'>{content}</div>
}

export default Winner