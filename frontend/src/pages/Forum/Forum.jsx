// React Import
import React from 'react'
import { useState, useEffect } from 'react'

// My Component Import
import ForumPage from "./ForumPage";

// API
import { getRequest } from "../../api/posts"

export default function Forum() {
    console.log("loading topics")

    var communityID = 798; // TODO | TO DYNAMICALLY LOAD IN LATER

    const [categories, setCategories] = useState([]);
    const [communities, setCommunities] = useState([]);    
    const [dataLoaded, setDataLoaded] = useState(false);    

    // Get All Communities (and then filter based on user auth to display relevant communities)
    useEffect(() => {
        const fetchCommunities = async() => {
          console.log("fetching communities api");
          try {
              const response = await getRequest('communities/', '');    // TODO | TO DYNAMICALLY LOAD IN LATER             
              setCommunities(communityID);  
              setDataLoaded(true);                     
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

    // Based on auth'd communities, get a list of the related threads
    useEffect(() => {
        const fetchCategories = async() => {
          console.log("fetching forum categories api");
          try {
              const response = await getRequest('categories/', '');
              console.log(response.data); 

              const myCategories = response.data.filter((category) => {
                return category.community === communities
              })         
              console.log(myCategories);
              setCategories(myCategories);         
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
      
        fetchCategories();
      
      }, [dataLoaded])
    
    return (
        <>
        <h1>Welcome to My Forum</h1>
        <ForumPage categories={categories}/>
        
        
        </>
    )
}