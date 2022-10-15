import { useEffect, useState } from "react"
import Channel from "../components/Channel"

export default function Home() {
  const [channels, setChannels] = useState([])
  let getChannelPosts = async ()=> {
    let response = await fetch('http://127.0.0.1:8000/channel', {
        method:'GET',
        headers:{
            'Content-Type':'application/json'
        },
    })
    let data = await response.json()
    setChannels(data)
    console.log(channels)
    console.log(data)
  }
  useEffect (()=> {
    getChannelPosts()
  }, []);

  return (
    <div className="grid grid-cols-3">
       {channels.map((props) =>
          <Channel props={props} />
      )}
    </div>
  ) 
}