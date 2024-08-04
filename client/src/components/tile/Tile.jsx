import PropTypes from 'prop-types';
import './Tile.css';

const Tile = props => {
    const style = props.tileNumber === 0 ? "tile empty" : "tile";
    return (
        <div className={style}>{props.tileNumber}</div>
    )
};

Tile.propTypes = {tileNumber: PropTypes.number.isRequired};

export default Tile;