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
                <div><div><i className='fa fa-search'/></div></div>
                <div><div><i className='fa fa-phone'/></div></div>
                <div><div><i className='fa fa-ellipsis-v'></i></div></div>
            </nav>
            <nav className='left-bar'>
                <div className='frame'>
                    <div className='search-bar'>
                        <div className='menu-icon'><div className='menu-icon2'> <i className='fa fa-bars'/></div></div>
                        <div className='frame-search'><div><i className='fa fa-search'/></div><input type="text" placeholder="Search" /></div>
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
                    <li><NavLink><i class="fa fa-address-book-o" style={{"font-size":"24px"}}></i></NavLink></li>
                    <li><NavLink><i className='fa fa-phone' style={{"font-size":"24px"}}></i></NavLink></li>
                    <li><NavLink><i className='fa fa-comment' style={{"font-size":"24px"}}></i></NavLink></li>
                    <li><NavLink><i className='fa fa-address-card-o' style={{"font-size":"24px"}}></i></NavLink></li>
                    <li><NavLink><i className='fa fa-gear' style={{"font-size":"24px"}}></i></NavLink></li>
                </ul>
            </nav>
            <div className='input-bar'>
                <div><i className="fa fa-smile-o"></i></div>
                <input type="text" placeholder='Message' />
                <div><i className="fa fa-sent-o"></i></div>
            </div>
        </div>
    )
}

export default Homepage;