import './Homepage.css';
import { NavLink } from 'react-router-dom';
import { Outlet } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import { useRef, useState ,useEffect} from 'react';
import { useContext } from 'react';
import { Context } from './Context';
import Contact from './Contact';
import Chat from './Chat-list';
import Topbar from './Top-bar';
import Allcards from './All-cards';
import Get_Send_Msg from './Get_Send_Msg';

function Homepage(ten){
    console.log(ten,'++')
    let func = true
    let [show_tab_bar, setShowTabBar]=useState(func)
    let [color_contact, setCCont] = useState('grey')
    let [color_chat,setCC] = useState()
    let [color_friends, SetCF] = useState()
    let [color_call, setCCall] = useState()
    let [color_settings, setCS] = useState()
    let [chat, setChat] = useState(true)
    let [contact, setContact] = useState(false)
    let [voicebutton, setVoiceButton] = useState(true)
    let [val, setVal] = useState();
    let textAreaRef = useRef(null);

    let resizeTextArea = () => {                 /* message yazilan textarea-sini avtomatik genislediren funksiya*/
        textAreaRef.current.style.height = "auto";
        textAreaRef.current.style.height = textAreaRef.current.scrollHeight + "px";
      };

    useEffect(resizeTextArea, [val]);

    const onChange = e => {
        setVal(e.target.value);
    };

    function Chat(){
        setChat(true)
        setContact(false)
    }
    function Contact(){
        setContact(true)
        setChat(false)
    }

    console.log(val)
    return(
        <div className='main'>
            {show_tab_bar==true?<div className='tab-bar-menu'>
                <NavLink to='/' className={({ isActive }) =>isActive ? setCC('#37A2DE') : setCC('#7C7C7C')} onClick={Chat} style={({isActive})=>({"background":isActive?"#D2ECFF":null})}><i className='far fa-comment'  style={{"fontSize":"21px","WebkitTextStroke":"0.5px #FFFFFF ","color":color_chat}}></i></NavLink>
                <NavLink to='/users' className={'active'?(color_friends='#37A2DE'):null}><i className='far fa-address-card' style={{color_friends}} ></i></NavLink>
                <NavLink to='/call'className={({ isActive }) =>isActive ? setCCont('#37A2DE') : setCCont('#7C7C7C')} ><i className="material-icons" style={{"color":color_call}}>add</i></NavLink>
                <NavLink to='/contact' onClick={Contact} className={({ isActive }) =>isActive ? setCCont('#37A2DE') : setCCont('#7C7C7C')} style={({isActive})=>({"background":isActive?"#D2ECFF":null})}><i className="material-icons" style={{"color":color_contact}}>person_outline</i></NavLink>
                <NavLink to='/settings'><span className="material-symbols-outlined" style={{"color":color_settings}}>settings</span></NavLink>
            </div>:null}
            <div className='left_side_bar'>
                <Chat/>
                <Outlet/>
            </div>
            <div>
                
            </div>
            <div className='Top-bar'>
                <Topbar/>
                
            </div>
            <div>
                <Get_Send_Msg/>
            </div>
            <div className='input'>
                <div>
                    <button><span class="material-symbols-outlined">sentiment_satisfied</span></button>
                    <textarea type="text" placeholder='Message' ref={textAreaRef} value={val} onChange={onChange} onInput={(e)=>{setVal(val=e.target.value);if(val.length!=0){setVoiceButton(false)};if(val.length==0){setVoiceButton(true)}}}/>
                    <button><span class="material-symbols-outlined" style={{"transform":"rotate(10deg)"}}>attach_file</span></button>
                </div>
                <div>
                    <button>
                        {voicebutton==true?<span class="material-symbols-outlined">mic</span>:<span class="material-symbols-outlined">send</span>}
                    </button>
                </div>
            </div>
        </div>
    )
}

export default Homepage;