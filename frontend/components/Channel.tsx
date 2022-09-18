import React from 'react'
import Post from './Post'
import Image from 'next/image'

function Channel({ props }:any) {
  const name = props.name // looks ugly but works (wtf)
  return (
    <div className='m-4 w-96'>
      <div className='flex flex-row justify-center items-center'>
        <h1>{name}</h1>
        <img src={props.logo} width={46} height={46} className="flex flex-row justify-center items-center"/>
     
      </div>
       {props.news.map((props: any) =>
        <Post props={props} channel={name}/>
      )}
    </div>
  )
}

export default Channel