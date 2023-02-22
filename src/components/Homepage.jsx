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
            <div className='homepage'>

            </div>
        </div>
    )
}

export default Homepage;