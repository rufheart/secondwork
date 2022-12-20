import logo from './logo.svg';
import './App.css';
import { Routes, Route } from 'react-router-dom';
import Chat,{Message, Card} from './components/Chat';

function App() {
  return (
    <Routes>
        <Route path='' element={<Chat/>}>
          <Route path='messages/:userName/:id' element={<Message />} />
        </Route>
        <Route path='/card' element={<Card/>}/>
    </Routes>
  );
}

export default App;
