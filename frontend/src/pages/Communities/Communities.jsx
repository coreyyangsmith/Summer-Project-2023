// React Import
import React, { useEffect, useState } from 'react'

// Component Imports
import CommunityPage from './CommunityPage'

// My Hooks
import { useCommunities } from '../../hooks/useCommunities'

const Communities = () => {

  // My Hooks
  const { communities, setCommunities } = useCommunities();

  return (
  <>
    <div>Communities</div>
    <CommunityPage communities={communities}/>
  </>
  )
}

export default Communities