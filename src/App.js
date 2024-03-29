import logo from './logo.svg';
import './App.css';
import { Routes, Route } from 'react-router-dom';
// import Chat, {Card} from './components/Chat';
import Message from './components/Message';
import Cards from './components/Cards';
import Welcome from './components/Wellcome';
import Homepage from './components/Homepage';
import Contact from './components/Contact';
import Chat from './components/Chat-list';
// import Get_Send_Msg from './components/Get_Send_Msg';
import Topbar from './components/Top-bar';

function App() {
  return (
    <Routes>
        <Route path='/' element={<Homepage/>}>
          <Route path='' element={<Chat/>}>
            {/* <Route path='messages/:userName/:id' element={<Get_Send_Msg/>}>
              <Route path='' element={<Topbar/>}/>  
            </Route>  */}
          </Route>
          <Route path='/contact' element={<Contact/>}/>
          {/* <Route path='messages/:userName/:id' element={<Get_Send_Msg/>}/> */}
          {/* <Route path='' element={<Welcome />} />*/}
          
        </Route>
    </Routes>
  );
}

export default App;
