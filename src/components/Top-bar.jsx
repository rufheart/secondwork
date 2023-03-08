import './Top-bar.css';
import { NavLink } from 'react-router-dom';
import { Outlet } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import { useRef, useState } from 'react';
import { useContext } from 'react';
import { Context } from './Context';

function Topbar(){
    let [showchatmenu, setShowChatMenu] = useState(false)
    function ShowChatMenu(){
        setShowChatMenu(!showchatmenu)
    }
    return(
        <div className='top-bar'>                   
            <NavLink className='other-user'>
                <img src="" alt="" />
                <div className='texts'>
                    <div><p>Lele S</p></div>
                    <div><p>5 min ago</p></div>
                </div>
            </NavLink>
            <NavLink>
                <div><div><i className="material-icons">search</i></div></div>
                <div><div><i className="material-icons" style={{"fontSize":"20px"}}>phone</i></div></div>
                <div><div><i className='fa fa-ellipsis-v' onClick={ShowChatMenu}></i></div></div>                
            </NavLink>
            {showchatmenu==true?
            <div>
                <button><span><span class="material-symbols-outlined">videocam</span></span>Video Call</button>
                <button><span><span class="material-symbols-outlined">mic</span></span>Mute notifications</button>
                <button><span><span class="material-symbols-outlined">flag</span></span>Report</button>
                <button><span><span class="material-symbols-outlined">delete</span></span>Delete chat</button>
                <button><span><span class="material-symbols-outlined">block</span></span>Block</button>
            </div>
            :null}
        </div>           
    )
}

export default Topbar;