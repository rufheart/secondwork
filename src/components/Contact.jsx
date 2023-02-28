import './Contact.css';
import { NavLink } from 'react-router-dom';
import { Outlet } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import { useRef, useState } from 'react';
import { useContext } from 'react';
import { Context } from './Context';

function Contact(){
    return(
        <ul className='contact-main'>
            <li>
                <NavLink>
                    <div>
                        <p>Gozlemede</p>
                        <div><i className='far fa-address-card'></i></div>
                    </div>
                    <div>
                        <p>Movcuddur</p>
                        <div><i className='far fa-address-card'></i></div>
                    </div>
                    <div></div>
                    <div></div>
                    <div>
                        <img src="" alt="" />
                        <p>Ad Soyad</p>
                    </div>
                    <div></div>
                </NavLink>
            </li>
        </ul>
    )
}

export default Contact;