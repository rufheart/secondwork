import { createContext, useContext } from "react";
import { useState, useEffect } from "react";

let Context = createContext();

function Provider({children}){

    let deyer = [
        {
            id:2,
            username:'Rufat',
            image:"",
            text:'standart'
        },
        {
            id:4,
            username:'Asif',
            image:"",
            text:'standart-17'
        },
    ]

    console.log(deyer,'context')
    return(
        <Context.Provider  value={{deyer}}>
            {children}
        </Context.Provider>
    )
}

export {Context}
export default Provider;