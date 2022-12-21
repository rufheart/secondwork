import './Chat.css'
import { NavLink } from 'react-router-dom';

function Cards(){
    return(
        <div>
            <div className='cards'>
                Cards
            </div>
            <ul>
                <li><NavLink to='/'>Chat</NavLink></li>
                <li><NavLink>About</NavLink></li>
                <li><NavLink>Contact</NavLink></li>
            </ul>
        </div>

    )
}

export default Cards;