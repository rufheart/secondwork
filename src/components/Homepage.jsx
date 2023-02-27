import './Homepage.css';
import { NavLink } from 'react-router-dom';
import { Outlet } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import { useRef, useState } from 'react';
import { useContext } from 'react';
import { Context } from './Context';


function Homepage(){
    return(
        <div className='main'>
            <nav className='top-bar'>
                <div className='other-user'>
                    <img src="" alt="" />
                    <div className='texts'>
                        <div><p>Lele S</p></div>
                        <div><p>5 min ago</p></div>
                    </div>
                </div>
                <div><div><i class="material-icons">search</i></div></div>
                <div><div><i className='fa fa-phone'/></div></div>
                <div><div><i className='fa fa-ellipsis-v'></i></div></div>
            </nav>
            <nav className='left-bar'>
                <div className='frame'>
                    <div className='search-bar'>
                        <div className='menu-icon'><div className='menu-icon2'> <i className='fa fa-bars' aria-hidden="true"/></div></div>
                        <div className='frame-search'><div><i class="material-icons">search</i></div><input type="text" placeholder="Search" /></div>
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
                <ul className='tab-bar-menu'>
                    <li><NavLink><i class="material-icons">person_outline</i></NavLink></li>
                    <li><NavLink><i className='fas fa-phone-alt' style={{"font-size":"22px"}}></i></NavLink></li>
                    <li><NavLink><i className='far fa-comment' style={{"font-size":"24px"}}></i></NavLink></li>
                    <li><NavLink><i className='far fa-address-card' style={{"font-size":"24px"}}></i></NavLink></li>
                    <li><NavLink><i className='fas fa-gear' style={{"font-size":"24px"}}></i></NavLink></li>
                </ul>
            </nav>
            <div className='input-bar'>
                <div><i className="far fa-smile"></i></div>
                <input type="text" placeholder='Message' />
                <div><i class="material-icons">send</i></div>
            </div>
        </div>
    )
}

export default Homepage;