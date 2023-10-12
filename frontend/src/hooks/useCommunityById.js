//-------------------------------------------------------//
//  File Name: useCommunityById.js
//  Description: Data Fetching Hook to a single "Community" model from the local database, given an ID
//
//  Requirements:
//      - /api/posts (axios)
//
//  Returns:
//      - Single Community Objects
//
// Created By: Corey Yang-Smith
// Date: October 12th, 2023
//-------------------------------------------------------//


//  IMPORTS
//-------------------------------------------------------//

// React Import
import { useEffect, useState } from "react"

// API Import
import { getRequest } from "../api/posts"


//  MAIN FUNCTION
//-------------------------------------------------------//

export const useCommunityById = (id) => {
    const [community, setCommunity] = useState([]);

    const fetchCommunity = async() => {
        try {
            const response = await getRequest("communities/", ''); 
            const myCommunity = response.data.filter((community) => {
                return community.id === id;
            }) 
            setCommunity(myCommunity);         
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

    useEffect(() => {
        fetchCommunity();
    }, []);

    return { community, setCommunity };
};
