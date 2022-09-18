import React, { useState } from 'react'

function Post({ props, channel }:any) {
  const time = new Date(props.created_at * 1); // why the fuck do i have to multiply this by 1???
  return (
    <div className='m-4'>
      <a href={props.link} className="block overflow-hidden rounded-2xl">
  <img
    src={props.img}
    className="object-cover w-full h-56"
  />

  <div className="p-4 bg-gray-900">
    <p className="text-xs text-gray-500">{channel}</p>

    <h5 className="text-sm text-white">
      {props.title}
    </h5>

    <p className="mt-1 text-xs text-gray-500">
      {time.toLocaleDateString()}
      <br></br>
      {"registrert " + time.toLocaleTimeString('NO', { hour: "numeric", 
                                             minute: "numeric"})
}
    </p>
  </div>
</a>
    </div>
  )
}

export default Post