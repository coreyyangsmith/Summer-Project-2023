// React Import
import React from 'react'

// My Component Import
import Categories from "./Categories"
import ForumCard from './ForumCard'

// MUI Import
import { Grid } from '@mui/material'

const ForumPage = (props) => {
  console.log("loading forum page")

  
    // Map Incoming
    const myCategories = props.categories.map(category => {
      return (
      <React.Fragment key={category.pk}> 
        <ForumCard category={category}/>
      </React.Fragment>
    )})   

  return (
    <>
  <Grid container spacing={2}>
        {myCategories}
    </Grid>
    </>
  )
}

export default ForumPage