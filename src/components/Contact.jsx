import './Contact.css';
import { NavLink } from 'react-router-dom';
import { Outlet } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import { useRef, useState } from 'react';
import { useContext } from 'react';
import { Context } from './Context';

function Contact(){
    return(
        <div className='contact-main'>
            <div>
                <div>
                    <NavLink>
                        <div>
                            <div>
                                <div>
                                    <p>Gozlemede</p>
                                    <div><i className='far fa-address-card' style={{"font-size":"24px"}}></i></div>                                    
                                </div>
                                <div></div>
                            </div>   
                            <div>
                                <img src="" alt="" />
                                <p>Ad Soyad</p>
                            </div>
                        </div>
                        <div>
                            <div></div>
                            <div>
                                <p>Movcuddur</p>
                                <div><i className='far fa-address-card' style={{"font-size":"24px"}}></i></div>                                
                            </div>
                        </div>
                    </NavLink>                    
                </div>
                <div><p>Invite to Chatgram</p></div>
                <div>
                    <div>
                        <div>
                            <img src="" alt="" />
                            <p>Elizabeta Fernandes</p>
                        </div>
                        <button>Invite</button>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Contact;