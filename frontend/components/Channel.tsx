import React from 'react'
import Post from './Post'
import Image from 'next/image'

function Channel({ props }:any) {
  const name = props.name // looks ugly but works (wtf)
  const color = props.color
  return (
    <div className='m-4 w-96 box-border border-4 overflow-y-scroll h-3/6'>
      <div>
        <img src={props.logo} width={1000} height={1000}/>
      </div>
      <div>
      {props.news.map((props: any) =>
        <Post props={props} channel={name} color={color} />
      )}
      </div>
    </div>
  )
}

export default Channel