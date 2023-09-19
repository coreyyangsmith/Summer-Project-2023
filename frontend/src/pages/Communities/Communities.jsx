import React, { useEffect } from 'react'

useEffect(() => {
  fetchCommunities(() => {

  })

  fetchCommunities();

}, [])

const Communities = () => {
  return (
    <div>Communities</div>
  )
}

export default Communities