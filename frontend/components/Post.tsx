import React, { useState } from 'react'

function Post({ props, channel, color }:any) {
  console.log(color)
  const time = new Date(props.created_at * 1); // why the fuck do i have to multiply this by 1???
  return (
    <div className='m-4'>
      <a href={props.link} className="block overflow-hidden rounded-2xl">
        <div className="p-4" style={{ backgroundColor: color }}>
          <p className="text-xs text-black">{channel}</p>

          <h5>
            {props.title}
          </h5>

          <p className="mt-1 text-xs text-black bold">
            {time.toLocaleDateString()}
            <br></br>
            {"registrert " + time.toLocaleTimeString('NO', { hour: "numeric", minute: "numeric"})}
          </p>
        </div>
      </a>
    </div>
  )
}

export default Post