import './Chat.css';
import { NavLink } from 'react-router-dom';
import { Outlet } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import { useRef, useState } from 'react';

function Chat(){
    let num1 = '1'
    let [show, setShow] = useState(true);
    let nav = useRef()
    function showNav(){
        if(show){
            setShow(!show)
            nav.current.style.left = '0'
        }else{
            setShow(!show)
            console.log('asasa', nav)
            nav.current.style.left = '-40%'
        }
        }   
    return(
        <div className="chat">
            <nav ref={nav}>
                <ul>
                    <li><NavLink to={`/messages/muxtar/${num1}`}>Muxtar</NavLink> </li>
                    <li><NavLink to={`/messages/rufet/${num1}`}>Rufet</NavLink> </li>
                </ul>
                <ul>
                    <li><NavLink to='/card'>Card</NavLink></li>
                    <li><NavLink>About</NavLink></li>
                    <li><NavLink>Contact</NavLink></li>
                </ul>
            </nav>
            
            <div className="messages-chat">
                <div className="welcome">
                    welecome 
                </div>
                <Outlet />
            </div>
            <div className="show" onClick={showNav}>show</div>

        </div>
    )
}


// function Message(){
//     console.log('message isledi')
//     let params = useParams();
//     return(
//         <div className="main-message">
//              <div className="header">Header 
//              </div>
//             <div className="messages">{params.userName}</div>
//         </div>
     
//     )
// }


// function Card(){
//     return(
//         <div className='cards'>
//             Cards
//         </div>
//     )
// }


export default Chat;
