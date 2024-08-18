import './Action.css'

const Action = ({action, actionText}) =>
    <div className='button-wrapper'>
        <button onClick={action}>{actionText}</button>
    </div>

export default Action