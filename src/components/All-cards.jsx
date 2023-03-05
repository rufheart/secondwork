import './All-cards.css';
import { NavLink } from 'react-router-dom';
import { Outlet } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import { useRef, useState } from 'react';
import { useContext } from 'react';
import { Context } from './Context';


function Allcards(){
    return(
        <div>
            <div className='all-card-top'>
                <h1>All cards(138)</h1>
                <div><input type="text" /><span><i className="material-icons">search</i></span></div>
                <div>Time <span><i className="material-icons">expand_more</i></span></div>
                <div>Salary <span><i className="material-icons">expand_more</i></span></div>
                <div>Location <span><i className="material-icons">expand_more</i></span></div>
            </div>
            <div className='all-card-info'>
                <card>
                    <div><span><span class="material-symbols-outlined">groups</span></span>Children</div>
                    <div><span><span class="material-symbols-outlined">phone_enabled</span></span>Phone</div>
                    <div><span><span class="material-symbols-outlined">groups</span></span>Picture</div>
                    <div><span><span class="material-symbols-outlined">phone_enabled</span></span>Address</div>
                    <div><span><span class="material-symbols-outlined">groups</span></span>Favorite places</div>
                    <div><span><span class="material-symbols-outlined">groups</span></span>Company</div>
                    <div><span><span class="material-symbols-outlined">groups</span></span>Name, Surname</div>
                    <div><span><span class="material-symbols-outlined">groups</span></span>Car number</div>
                    <div><span><span class="material-symbols-outlined">person</span></span>Relationships</div>
                    <div><span><span class="material-symbols-outlined">person</span></span>Social Accounts</div>
                    <div><span><span class="material-symbols-outlined">phone_enabled</span></span>Relevant person</div>
                    <div><span><span class="material-symbols-outlined">groups</span></span>Community</div>
                    <div>Add to cart</div>
                    <h1>699.99$</h1>
                    <div>
                        <div>
                            <div><p>4.5</p><span class="material-symbols-outlined">star</span></div>
                            <div></div>
                            <p>243 comments</p>
                        </div>
                        <div>
                            <div>
                                <div><span class="material-symbols-outlined">favorite</span></div>
                                <p>421</p>
                            </div>
                        </div>
                    </div>
                    <div></div>
                    <div>
                        <div>
                            <img src="" alt="" />
                            <div>
                                <p>Eliyev Veli Rasim</p>
                                <div><span><span class="material-symbols-outlined">location_on</span></span><p>Baku, Azerbaijan</p></div>
                            </div>
                        </div>
                    </div>
                    <div></div>
                </card>
            </div>
        </div>
    )
}

export default Allcards;