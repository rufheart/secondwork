import './Contact.css';
import { NavLink } from 'react-router-dom';
import { Outlet } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import { useRef, useState } from 'react';
import { useContext } from 'react';
import { Context } from './Context';

function Contact(){
    return(
        <nav className='contact-main'>
            <div>
                <div><span class="material-symbols-outlined">arrow_back</span></div>                
                <div>                    
                    <div><i class="material-icons">search</i></div>
                    <input type="text" placeholder='Search'/>
                </div>
            </div>
            <NavLink>
                <div>
                    <p>Gozlemede</p>
                    <div><i className='far fa-address-card' style={{"font-size":"24px"}}></i></div>
                </div>
                <div>
                    <p>Movcuddur</p>
                    <div><i className='far fa-address-card' style={{"font-size":"24px"}}></i></div>
                </div>
                <div></div>
                <div></div>
                <div>
                    <img src="" alt="" />
                    <p>Ad Soyad</p>
                </div>
                <div></div>
            </NavLink>
            <div><p>Invite to Chatgram</p></div>
        </nav>
    )
}

export default Contact;