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
            <div className='left-bar'>
                <div className='search-bar'>
                    <div className='menu-icon'><div className='menu-icon2'> <i className='fa fa-bars'/></div></div>
                    <div className='frame-search'><i className='fa fa-search'/><input type="text" /></div>
                </div>
                <div className='chat-list'>
                    
                </div>
            </div>
        </div>
    )
}

export default Homepage;