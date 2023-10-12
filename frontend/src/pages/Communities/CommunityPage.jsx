// React Import 
import React from 'react'

// MUI Import
import { Grid } from '@mui/material'

// Components Import
import CommunityCard from './CommunityCard'
import CommunityFilter from './CommunityFilter'

// Community Page Holds Page Logic
const CommunityPage = (props) => {

  let myCommunities = <p>Loading...</p>;
  
  if (props.communities != undefined)
  {
    // Map Incoming
    myCommunities = props.communities.map(community => {
      return (
      <React.Fragment key={community.pk}> 
        <CommunityCard community={community}/>
      </React.Fragment>
    )})   
  }

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