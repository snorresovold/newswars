export default function Home() {
  let getChannelPosts = async ()=> {
    let response = await fetch('http://127.0.0.1:8000/channel', {
        method:'GET',
        headers:{
            'Content-Type':'application/json'
        },
    })
    let data = await response.json()
    console.log(data)
  }
  getChannelPosts()
  return (
    <div className="grid grid-cols-2">
    </div>
  ) 
}