import './Chat-list.css';
import { NavLink } from 'react-router-dom';
import { Outlet } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import { useRef, useState } from 'react';
import { useContext } from 'react';
import { Context } from './Context';



function Chat(){
    return(
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
    )
}

export default Chat;