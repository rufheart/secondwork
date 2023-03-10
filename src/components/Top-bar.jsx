import './Top-bar.css';
import { NavLink } from 'react-router-dom';
import { Outlet } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import { useRef, useState,useEffect } from 'react';
import { useContext } from 'react';
import { Context } from './Context';

function Topbar(){
    let [showchatmenu, setShowChatMenu] = useState(false)
    let [deletechat,setDeleteChat] = useState(false)
    let menuRef=useRef();
    useEffect(()=>{
        let handler=(e)=>{
            if(!menuRef.current.contains(e.target)){
                setShowChatMenu(false)
                setDeleteChat(false)
            }            
        };
        document.addEventListener("mousedown",handler)
        return()=>{
            document.removeEventListener("mousedown", handler)
        }
    });

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
                <div><div><i className='fa fa-ellipsis-v' onClick={()=>(setShowChatMenu(!showchatmenu),setDeleteChat(false))}></i></div></div>                
            </NavLink>
            <div>
                {showchatmenu==true?
                    <div ref={menuRef}>
                        <button><span><span class="material-symbols-outlined">videocam</span></span>Video Call</button>
                        <button><span><span class="material-symbols-outlined">mic</span></span>Mute notifications</button>
                        <button><span><span class="material-symbols-outlined">flag</span></span>Report</button>
                        <button onClick={()=>(!setDeleteChat(true),setShowChatMenu(false),console.log('yes'))}><span><span class="material-symbols-outlined">delete</span></span>Delete chat</button>
                        <button><span><span class="material-symbols-outlined">block</span></span>Block</button>
                    </div>
                :null}                
            </div>
            <div className='delete_chat_tab' >
                {deletechat==true?
                    <div ref={menuRef}>
                        <div className='top'><p>Delete this chat?</p><p>Permanently delete the chat with ME Me?</p></div>
                        <div className='buttom'><button onClick={()=>setShowChatMenu(false)}>CANCEL</button><button>DELETE CHAT</button></div>      
                    </div>:null                       
                }
            </div>              
        </div>           
    )
}

export default Topbar;