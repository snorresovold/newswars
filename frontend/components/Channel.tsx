import React from 'react'
import Post from './Post'

function Channel({ props }:any) {
  const name = props.name // looks ugly but works
  return (
    <div className='m-4 w-96'>
      <h1 className='flex flex-row justify-center items-center'>{name}</h1>
      {props.news.map((props: any) =>
        <Post props={props} channel={name}/>
      )}
    </div>
  )
}

export default Channel