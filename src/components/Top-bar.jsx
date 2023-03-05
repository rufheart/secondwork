import './Top-bar.css';
import { NavLink } from 'react-router-dom';
import { Outlet } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import { useRef, useState } from 'react';
import { useContext } from 'react';
import { Context } from './Context';

function Topbar(){
    return(
        <div className='top-bar'>                   
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
        </div>           
    )
}

export default Topbar;