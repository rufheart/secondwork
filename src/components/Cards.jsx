import './Chat.css'
import { NavLink } from 'react-router-dom';

function Cards(){
    return(
        <div className='cards'>
            <div className='card'>
                Cards
            </div>
            <div>
                <ul>
                    <li><NavLink to='/'>Chat</NavLink></li>
                    <li><NavLink>About</NavLink></li>
                    <li><NavLink>Contact</NavLink></li>
                </ul>
            </div>
        </div>

    )
}

export default Cards;