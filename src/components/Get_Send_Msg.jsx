import './Get_Send_Msg.css';
import { NavLink } from 'react-router-dom';
import { Outlet } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import { useRef, useState } from 'react';
import { useContext } from 'react';
import { Context } from './Context';


function Get_Send_Msg(){
    return(
        <div className='sendandget'>
            <div className='your'><div></div></div>
            <div className='sender'><div></div></div>
        </div>
    )
}

export default Get_Send_Msg;