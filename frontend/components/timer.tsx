import React from 'react'
import { useState, useEffect } from 'react';

function minuteCount(minutesAfterHour: any) {

    const now          = new Date();
    const hours        = now.getHours();
    const minutes      = now.getMinutes();
    const seconds      = now.getSeconds();
    const milliseconds = now.getMilliseconds();

    const waitUntilNextMinute = setTimeout(minuteCount, 60000 - seconds * 1000 - milliseconds);

    if(minutes % 60 === minutesAfterHour) {
        console.log("sus")
    }

}

minuteCount(45);

const Timer = () => {
    const now = new Date();
    const [ minutes, setMinutes ] = useState(now.getMinutes());
    const [ seconds, setSeconds ] =  useState(now.getSeconds());

    const TimeHandler = () => {
        let myInterval = setInterval(() => {
            now.getMinutes()
        })

        return(
            myInterval
        );
    }
    
    useEffect(()=>{

        let myInterval = setInterval(() => {
                if (seconds > 0) {
                    setSeconds(seconds - 1);
                }
                if (seconds === 0) {
                    if (minutes === 0) {
                        clearInterval(myInterval)
                    } else {
                        setMinutes(minutes - 1);
                        setSeconds(59);
                    }
                } 
            }, 1000)
            return ()=> {
                clearInterval(myInterval);
            };
        });

    return (
        <div>
            <h1>hello</h1>
        </div>
    )
}

export default Timer;