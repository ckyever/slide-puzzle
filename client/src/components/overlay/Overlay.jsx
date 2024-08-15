import './Overlay.css'

const Overlay = ({numberOfTiles}) => 
    new Array(numberOfTiles).fill().map((_,i) => <div key={i} className="overlay"/>)

export default Overlay
