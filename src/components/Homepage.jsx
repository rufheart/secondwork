import './Homepage.css';
import { NavLink } from 'react-router-dom';
import { Outlet } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import { useRef, useState } from 'react';
import { useContext } from 'react';
import { Context } from './Context';
import Contact from './Contact';
import Chat from './Chat-list';
import Topbar from './Top-bar';
import Allcards from './All-cards';

function Homepage(){
    let [color_contact, setCCont] = useState('grey')
    let [color_chat,setCC] = useState()
    let [color_friends, SetCF] = useState()
    let [color_call, setCCall] = useState()
    let [color_settings, setCS] = useState()
    let [chat, setChat] = useState(true)
    let [contact, setContact] = useState(false)
    function Chat(){
        setChat(true)
        setContact(false)
    }
    function Contact(){
        setContact(true)
        setChat(false)
    }
    let activeStyle = {
        chart
      };
    function chart(){
        console.log('vhart')
    }
    return(
        <div className='main'>
            <nav >
                <Allcards/>
                {/* <Topbar/> */}
                {/* <Outlet/> */}
            </nav>
            <nav className='left-bar'>
                <div className='left-bar-top'>
                    {/* {<Chat/>} */}
                    {contact==true?<Contact/>:null}
                    <Outlet/>
                </div>
                <div className='tab-bar-menu'>
                    <NavLink to='/contact' onClick={Contact} className={({ isActive }) =>isActive ? setCCont('#37A2DE') : setCCont('#7C7C7C')}><i className="material-icons" style={{"color":color_contact}}>person_outline</i></NavLink>
                    <NavLink to='/call'className={({ isActive }) =>isActive ? setCC('#37A2DE') : setCC('#7C7C7C')} ><i className="material-icons" style={{"color":color_call}}>phone</i></NavLink>
                    <NavLink to='/' className={({ isActive }) =>isActive ? setCC('#37A2DE') : setCC('#7C7C7C')} onClick={Chat}><i className='far fa-comment'  style={{"fontSize":"21px","WebkitTextStroke":"0.5px #FFFFFF ","color":color_chat}}></i></NavLink>
                    <NavLink to='/users' className={'active'?(color_friends='#37A2DE'):null}><i className='far fa-address-card'style={{color_friends}} ></i></NavLink>
                    <NavLink to='/settings'><span className="material-symbols-outlined" style={{"color":color_settings}}>settings</span></NavLink>
                </div>
            </nav>
            <div className='input-bar'>
                <div><i className="far fa-smile"></i></div>
                <input type="text" placeholder='Message' />
                <div><i className="material-icons">send</i></div>
                
            </div>
            <div className='background'>

            </div>
        </div>
    )
}

export default Homepage;