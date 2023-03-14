import './Chat-list.css';
import { NavLink } from 'react-router-dom';
// import { Outlet } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import { useRef, useState,useEffect} from 'react';
import { useContext } from 'react';
import { Context } from './Context';
import Homepage from './Homepage';



function Chat(){
    let [chalistshow, setChatListShow] = useState(true)
    let [activecolor, setAcColor] = useState()
    let [activecolor2, setAcColor2] = useState()
    let [smsbackground, setSmsBackGround] = useState()
    let [smscolor, setSmsColor] = useState()
    let [showmenu, setShowMenu] = useState(false)
    let [newcontact, setNewContact] = useState(false)
    let menuRef=useRef();
    useEffect(()=>{
        let handler = (e)=>{
            if(!menuRef.current.contains(e.target)){
                setShowMenu(false)
                setNewContact(false)
            }
        };
        document.addEventListener("mousedown",handler)

        return()=>{
            document.removeEventListener("mousedown", handler)
        }
    });
    return(
        <div>
            {chalistshow==false?<Homepage func={false}/>:<Homepage func={true}/>}
            {chalistshow==false?<div>
                <div></div>
                <div></div>
                <div>
                    <div><input type="checkbox" /></div>
                    <div></div>
                </div>
            </div>:null}
            {chalistshow==true?<div className='frame'>
            <div className='search-bar'  ref={menuRef}>
                <div className='menu-icon'><div className='menu-icon2'> <i className='fa fa-bars' aria-hidden="true" style={{"fontSize":"24px"}} onClick={()=>(setShowMenu(!showmenu),setNewContact(false))} /></div></div>
                <div className='frame-search'><div><i className="material-icons">search</i></div><input type="text" placeholder="Search" /></div>
                {showmenu==true?
               <div ref={menuRef}>
                    <button><span><span class="material-symbols-outlined">bookmark</span></span>Saved Cards</button>
                    <button onClick={()=>(setNewContact(!newcontact),setShowMenu(false))}><span><span class="material-symbols-outlined">person</span></span>New Contact</button>
                    <button onClick={()=>setChatListShow(false)}><span><span class="material-symbols-outlined">supervisor_account</span></span>New Group</button>
                    <button><span><span class="material-symbols-outlined">logout</span></span>Logout</button>
                </div>                    
                :null
                }
            </div>
            <ul className='chat-list'>
                <li>
                    <NavLink to={`messages/rufat/1`} style={({isActive})=>({"background":isActive?"#356CD2":"#FFFFFF"})} className={({isActive})=>isActive?(setAcColor("#FFFFFF"),setAcColor2("#FFFFFF"),setSmsBackGround('#FFFFFF'),setSmsColor('#356CD2')):(setAcColor("#262626"),setAcColor2("#565656"),setSmsBackGround('#356CD2'),setSmsColor('#FFFFFF'))}>
                        <img src={require('../panda.jpg')} alt="" />
                        <div className='chat-text'>
                            <div className='frame2'>
                                <div className='name'>
                                    <div  style={{"color":activecolor}}>Chatgram</div>
                                    <div><span class="material-symbols-outlined">verified</span></div>
                                </div>
                                <div style={{"color":activecolor2}}>09:25</div>
                            </div>
                            <div className='message' >
                                <p style={{"color":activecolor2}}>Chatgram verify code:45545</p>
                                <p style={{"background":smsbackground,"color":smscolor}}>2</p>
                            </div>                                
                        </div>                                
                    </NavLink>
                </li>
                <li>
                    <NavLink>
                        <img src="" alt="" />
                        <div className='chat-text'>
                            <div className='frame2'>
                                <div className='name'>
                                    <div>Chatgram</div>
                                    <div><i className='fa fa-check-circle'></i></div>
                                </div>
                                <div>09:25</div>
                            </div>
                            <div className='message'>
                                <p>Chatgram verify code:45545</p>
                                <p>2</p>
                            </div>                                
                        </div>                                
                    </NavLink>
                </li>
                <li>
                    <NavLink>
                        <img src="" alt="" />
                        <div className='chat-text'>
                            <div className='frame2'>
                                <div className='name'>
                                    <div>Chatgram</div>
                                    <div><i className='fa fa-check-circle'></i></div>
                                </div>
                                <div>09:25</div>
                            </div>
                            <div className='message'>
                                <p >Chatgram verify code:45545</p>
                                <p>2</p>
                            </div>                                
                        </div>                                
                    </NavLink>
                </li>
                <li>
                    <NavLink>
                        <img src="" alt="" />
                        <div className='chat-text'>
                            <div className='frame2'>
                                <div className='name'>
                                    <div>Chatgram</div>
                                    <div><i className='fa fa-check-circle'></i></div>
                                </div>
                                <div>09:25</div>
                            </div>
                            <div className='message'>
                                <p>Chatgram verify code:45545</p>
                                <p>2</p>
                            </div>                                
                        </div>                                
                    </NavLink>
                </li>
                <li>
                    <NavLink>
                        <img src="" alt="" />
                        <div className='chat-text'>
                            <div className='frame2'>
                                <div className='name'>
                                    <div>Chatgram</div>
                                    <div><i className='fa fa-check-circle'></i></div>
                                </div>
                                <div>09:25</div>
                            </div>
                            <div className='message'>
                                <p>Chatgram verify code:45545</p>
                                <p>2</p>
                            </div>                                
                        </div>                                
                    </NavLink>
                </li>
                <li>
                    <NavLink>
                        <img src="" alt="" />
                        <div className='chat-text'>
                            <div className='frame2'>
                                <div className='name'>
                                    <div>Chatgram</div>
                                    <div><i className='fa fa-check-circle'></i></div>
                                </div>
                                <div>09:25</div>
                            </div>
                            <div className='message'>
                                <p>Chatgram verify code:45545</p>
                                <p>2</p>
                            </div>                                
                        </div>                                
                    </NavLink>
                </li>
                <li>
                    <NavLink>
                        <img src="" alt="" />
                        <div className='chat-text'>
                            <div className='frame2'>
                                <div className='name'>
                                    <div>Chatgram</div>
                                    <div><i className='fa fa-check-circle'></i></div>
                                </div>
                                <div>09:25</div>
                            </div>
                            <div className='message'>
                                <p>Chatgram verify code:45545</p>
                                <p>2</p>
                            </div>                                
                        </div>                                
                    </NavLink>
                </li>
                <li>
                    <NavLink>
                        <img src="" alt="" />
                        <div className='chat-text'>
                            <div className='frame2'>
                                <div className='name'>
                                    <div>Chatgram</div>
                                    <div><i className='fa fa-check-circle'></i></div>
                                </div>
                                <div>09:25</div>
                            </div>
                            <div className='message'>
                                <p>Chatgram verify code:45545</p>
                                <p>2</p>
                            </div>                                
                        </div>                                
                    </NavLink>
                </li>
                <li>
                    <NavLink>
                        <img src="" alt="" />
                        <div className='chat-text'>
                            <div className='frame2'>
                                <div className='name'>
                                    <div>Chatgram</div>
                                    <div><i className='fa fa-check-circle'></i></div>
                                </div>
                                <div>09:25</div>
                            </div>
                            <div className='message'>
                                <p>Chatgram verify code:45545</p>
                                <p>2</p>
                            </div>                                
                        </div>                                
                    </NavLink>
                </li>
                <li>
                    <NavLink>
                        <img src="" alt="" />
                        <div className='chat-text'>
                            <div className='frame2'>
                                <div className='name'>
                                    <div>Chatgram</div>
                                    <div><i className='fa fa-check-circle'></i></div>
                                </div>
                                <div>09:25</div>
                            </div>
                            <div className='message'>
                                <p>Chatgram verify code:45545</p>
                                <p>2</p>
                            </div>                                
                        </div>                                
                    </NavLink>
                </li>
                <li>
                    <NavLink>
                        <img src="" alt="" />
                        <div className='chat-text'>
                            <div className='frame2'>
                                <div className='name'>
                                    <div>Chatgram</div>
                                    <div><i className='fa fa-check-circle'></i></div>
                                </div>
                                <div>09:25</div>
                            </div>
                            <div className='message'>
                                <p>Chatgram verify code:45545</p>
                                <p>2</p>
                            </div>                                
                        </div>                                
                    </NavLink>
                </li>
                <li>
                    <NavLink>
                        <img src="" alt="" />
                        <div className='chat-text'>
                            <div className='frame2'>
                                <div className='name'>
                                    <div>Chatgram</div>
                                    <div><i className='fa fa-check-circle'></i></div>
                                </div>
                                <div>09:25</div>
                            </div>
                            <div className='message'>
                                <p>Chatgram verify code:45545</p>
                                <p>2</p>
                            </div>                                
                        </div>                                
                    </NavLink>
                </li>                    
            </ul>
            <div>
                {newcontact==true?
                    <div className='new_contact_add' ref={menuRef}>
                        <div className='top'>
                            <p>New Contact</p>
                            <div>
                                <input type="text" placeholder='First name'/>
                                <input type="text" placeholder='Last name' />
                                <input type="text" placeholder='Phone number'/>
                            </div>
                        </div>
                        <div className='button'>
                            <button onClick={()=>setNewContact(false)}>Cancel</button>
                            <button>Create Contact</button>
                        </div>
                    </div> :null           
                }
            </div>  
        </div>:null}</div>     
    )
}

export default Chat;