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
            <nav className='left-bar'>
                <div className='search-bar'>
                    <div className='menu-icon'><div className='menu-icon2'> <i className='fa fa-bars'/></div></div>
                    <div className='frame-search'><div><i className='fa fa-search'/></div><input type="text" placeholder="Search" /></div>
                </div>
                <div className='chat-list'>
                    
                </div>
                <div className='tab-bar-menu'>
                    <div>soz</div>
                </div>
            </nav>
        </div>
    )
}

export default Homepage;