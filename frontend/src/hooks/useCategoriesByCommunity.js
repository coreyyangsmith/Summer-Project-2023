//-------------------------------------------------------//
//  File Name: useCategoriesByCommunity.js
//  Description: Data Fetching Hook to obtain all "Categories" models from the local database
//
//  Requirements:
//      - /api/posts (axios)
//
//  Returns:
//      - List of Community Objects
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

export const useCategoriesByCommunity = (id) => {
    const [categories, setCategories] = useState([]);

    const fetchCategoriesByCommunity = async() => {
        try {
            const response = await getRequest("categories/", '');   
            const categoriesByCommunity = response.data.filter((category) => {
                return category.community === id
            })
            setCategories(categoriesByCommunity);         
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
        fetchCategoriesByCommunity();
    }, []);

    return { categories, setCategories };
};
