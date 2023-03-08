import './Chat-list.css';
import { NavLink } from 'react-router-dom';
import { Outlet } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import { useRef, useState } from 'react';
import { useContext } from 'react';
import { Context } from './Context';



function Chat(){
    let [activecolor, setAcColor] = useState()
    let [showmenu, setShowMenu] = useState(false)
    function ShowMenu(){
        setShowMenu(!showmenu)
    }
    return(
        <div className='frame'>
            <div className='search-bar'>
                <div className='menu-icon'><div className='menu-icon2'> <i className='fa fa-bars' aria-hidden="true" style={{"fontSize":"24px"}} onClick={ShowMenu}/></div></div>
                <div className='frame-search'><div><i className="material-icons">search</i></div><input type="text" placeholder="Search" /></div>
                {showmenu==true?
               <div>
                <div><span><span class="material-symbols-outlined">bookmark</span></span>Saved Cards</div>
                <div><span><span class="material-symbols-outlined">person</span></span>New Contact</div>
                <div><span><span class="material-symbols-outlined">supervisor_account</span></span>New Group</div>
                <div><span><span class="material-symbols-outlined">logout</span></span>Logout</div>
                </div>                    
                :null
                }
            </div>
            <ul className='chat-list'>
                <li>
                    <NavLink style={({isActive})=>({"background":isActive?"#356CD2":null})} className={({isActive})=>isActive?setAcColor("#FFFFFF"):null}>
                        <img src="" alt="" />
                        <div className='chat-text'>
                            <div className='frame2'>
                                <div className='name'>
                                    <div  style={{"color":activecolor}}>Chatgram</div>
                                    <div><span class="material-symbols-outlined">verified</span></div>
                                </div>
                                <div  style={{"color":activecolor}}>09:25</div>
                            </div>
                            <div className='message' >
                                <p style={{"color":activecolor}}>Chatgram verify code:45545</p>
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
        </div>        
    )
}

export default Chat;