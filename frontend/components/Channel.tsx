import React from 'react'
import Post from './Post'

function Channel({ props }:any) {
  const name = props.name // looks ugly but works (wtf)
  const color = props.color
  return (
    <div className='grid grid-rows-4 m-4 w-96 box-border border-4 overflow-y-scroll h-96'>
      <div>
      {props.news.map((props: any) =>
        <Post props={props} channel={name} color={color} />
      )}
      </div>
    </div>
  )
}

export default Channel