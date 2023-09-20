// React Import
import React, { useEffect, useState } from 'react'

// Component Imports
import CommunityPage from './CommunityPage'


// API
import axios from 'axios'



const Communities = () => {
  console.log("loading Communities");
   const [communities, setCommunities] = useState([]);

   useEffect(() => {

    const fetchCommunities = async() => {
      console.log("fetching communities api");
      try {
          const response = await axios.get('http://127.0.0.1:8000/api/communities/', '');
          console.log(response.data);          
          setCommunities(response.data);         
      } catch (err) {
          if (err.response) {
              // Not in 200 response range
              console.log(err.response.data);
              console.log(err.response.status);
              console.log(err.response.headers);   
          }
          else {
              console.log(`Error: ${err.message}`);
          }                             
      }
    }        
  
    fetchCommunities();
  
  }, [])

  return (
  <>
    <div>Communities</div>
    <CommunityPage communities={communities}/>
  </>
  )
}

export default Communities