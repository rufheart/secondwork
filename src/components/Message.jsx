import { useParams } from 'react-router-dom';
import './Chat.css';

function Message(){
    console.log('message isledi')
    let params = useParams();
    return(
        <div className="main-message">
             <div className="header">Header 
             </div>
            <div className="messages">{params.userName}</div>
        </div>
     
    )
}

export default Message;