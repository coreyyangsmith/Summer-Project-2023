// React Import 
import React from 'react'

// MUI Import
import { Grid } from '@mui/material'

// Components Import
import CommunityCard from './CommunityCard'
import CommunityFilter from './CommunityFilter'

// Community Page Holds Page Logic
const CommunityPage = (props) => {
  console.log("loading CommunityPage");


  // Map incoming
  const myCommunities = props.communities.map(community => {
    return (
    <React.Fragment key={community.pk}> 
      <CommunityCard community={community}/>
    </React.Fragment>
  )})   


  return (
  <>
  <CommunityFilter/>
  <Grid container spacing={2}>
      {myCommunities}
  </Grid>
  </>
  )
}

export default CommunityPage