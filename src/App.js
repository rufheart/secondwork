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

function App() {
  return (
    <Routes>
        <Route path='/' element={<Homepage/>}>
          <Route path='' element={<Chat/>}/>
          <Route path='/contact' element={<Contact/>}/>
          {/* <Route path='' element={<Welcome />} />
          <Route path='messages/:userName/:id' element={<Message />} /> */}
        </Route>
    </Routes>
  );
}

export default App;
