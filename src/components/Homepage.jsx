import './Homepage.css';
import { NavLink } from 'react-router-dom';
import { Outlet } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import { useRef, useState } from 'react';
import { useContext } from 'react';
import { Context } from './Context';
import Contact from './Contact';


function Homepage(){
    let [color_contact, setCCont] = useState()
    let [color_chat,setCC] = useState()
    let [color_friends, SetCF] = useState()
    let [color_call, setCCall] = useState()
    let [color_settings, setCS] = useState()

    return(
        <div className='main'>
            <nav className='top-bar'>
                <NavLink className='other-user'>
                    <img src="" alt="" />
                    <div className='texts'>
                        <div><p>Lele S</p></div>
                        <div><p>5 min ago</p></div>
                    </div>
                </NavLink>
                <div><div><i className="material-icons">search</i></div></div>
                <div><div><i className="material-icons" style={{"fontSize":"20px"}}>phone</i></div></div>
                <div><div><i className='fa fa-ellipsis-v'></i></div></div>
            </nav>
            <nav className='left-bar'>
                <div className='frame'>
                    <div className='search-bar'>
                        <div className='menu-icon'><div className='menu-icon2'> <i className='fa fa-bars' aria-hidden="true"/></div></div>
                        <div className='frame-search'><div><i className="material-icons">search</i></div><input type="text" placeholder="Search" /></div>
                    </div>
                    <ul className='chat-list'>
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
                <div className='tab-bar-menu'>
                    <NavLink to='/contact'><i className="material-icons" style={{"color":color_contact}}>person_outline</i></NavLink>
                    <NavLink to='/call' ><i className="material-icons" style={{"color":color_call}}>phone</i></NavLink>
                    <NavLink to='/' className={'active'?(color_chat='#37A2DE'):null}><i className='far fa-comment'  style={{"fontSize":"21px","WebkitTextStroke":"0.5px #FFFFFF ","color":color_chat}}></i></NavLink>
                    <NavLink to='/users' className={'active'?(color_friends='#37A2DE'):null}><i className='far fa-address-card'style={{color_friends}} ></i></NavLink>
                    <NavLink to='/settings'><span className="material-symbols-outlined" style={{"color":color_settings}}>settings</span></NavLink>
                </div>
            </nav>
            <div className='input-bar'>
                <div><i className="far fa-smile"></i></div>
                <input type="text" placeholder='Message' />
                <div><i className="material-icons">send</i></div>
                
            </div>
        </div>
    )
}

export default Homepage;