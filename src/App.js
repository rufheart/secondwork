import logo from './logo.svg';
import './App.css';
import { Routes, Route } from 'react-router-dom';
import Chat, {Card} from './components/Chat';
import Message from './components/Message';
import Cards from './components/Cards';

function App() {
  return (
    <Routes>
        <Route path='' element={<Chat/>}>
          <Route path='messages/:userName/:id' element={<Message />} />
        </Route>
        <Route path='/card' element={<Cards/>}/>
    </Routes>
  );
}

export default App;
