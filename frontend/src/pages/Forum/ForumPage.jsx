// React Import
import React from 'react'

// My Component Import
import Categories from "./Categories"
import ForumCard from './ForumCard'

const ForumPage = (props) => {
  console.log("loading forum page")

  
    // Map Incoming
    const myCommunities = props.categories.map(category => {
      return (
      <React.Fragment key={category.pk}> 
        <ForumCard category={category}/>
      </React.Fragment>
    )})   






  return (
    <>
      {myCommunities}
    </>
  )
}

export default ForumPage