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
    let [blockshow, setBlockShow] = useState(false)
    let [reportshow, setReportShow] = useState(false)
    let params = useParams()
    let menuRef=useRef();
    useEffect(()=>{
        let handler=(e)=>{
            if(!menuRef.current.contains(e.target)){
                setShowChatMenu(false)
                setBlockShow(false)
                setReportShow(false)
                setDeleteChat(false)
                console.log('useeffect')
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
                    <div><p>{params.userName}</p></div>
                    <div><p>5 min ago</p></div>
                </div>
            </NavLink>
            <div>
                <button><span class="material-symbols-outlined">search</span></button>
                <button><i className="material-icons" style={{"fontSize":"20px"}}>phone</i></button>
                <button onClick={()=>(setShowChatMenu(!showchatmenu),setDeleteChat(false),console.log('3 noqte'))}><i className='fa fa-ellipsis-v' ></i></button>                
            </div>
            <div>
                {showchatmenu==true?
                    <div ref={menuRef}>
                        <button><span><span class="material-symbols-outlined">videocam</span></span>Video Call</button>
                        <button><span><span class="material-symbols-outlined">mic</span></span>Mute notifications</button>
                        <button onClick={()=>(setReportShow(!reportshow),setShowChatMenu(false))}><span><span class="material-symbols-outlined">flag</span></span>Report</button>
                        <button onClick={()=>(setDeleteChat(!deletechat),setShowChatMenu(false))}><span><span class="material-symbols-outlined">delete</span></span>Delete chat</button>
                        <button onClick={()=>(setBlockShow(!blockshow),setShowChatMenu(false))}><span><span class="material-symbols-outlined">block</span></span>Block</button>
                    </div>
                :null}                
            </div>
            <div >
                {deletechat==true?
                    <div  className='delete_chat_tab' ref={menuRef}>
                        <div className='top'><p>Delete this chat?</p><p>Permanently delete the chat with ME Me?</p></div>
                        <div className='buttom'><button onClick={()=>(setDeleteChat(false))}>CANCEL</button><button>DELETE CHAT</button></div>      
                    </div>:null                       
                }
                {blockshow==true?
                    <div className='block_tab' ref={menuRef}>
                        <div><p>Block Lele S?</p><p>Blocked contacts will no longer be able to call you or send you messages. This contact will not be notified. </p></div>
                        <div><button onClick={()=>setBlockShow(false)}>CANCEL</button><button>BLOCK</button></div>
                    </div>:null
                } 
                {reportshow==true?
                    <div className='report_tab' ref={menuRef}>
                        <div>
                            <div>
                                <div>Report this contact to Chatgram?</div>
                                <div><input type="checkbox"/><p>Block contact and clear chat</p></div>
                                <div>
                                    If you block this contact and clear the chat, message will only be removed from this deviceand your devices on the newer versions of Chatgram.                                
                                </div>
                            </div>
                            <div>This contact will not be notified</div>
                        </div>
                        <div>
                            <button onClick={()=>(setReportShow(false),console.log('yes'))}>CANCEL</button>
                            <button>REPORT</button>
                        </div>
                    </div>:null
                }      
            </div>              
        </div>           
    )
}

export default Topbar;