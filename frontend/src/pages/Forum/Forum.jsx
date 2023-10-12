// React Import
import React from 'react'
import { useState } from 'react'

// My Component Import
import ForumPage from "./ForumPage";
import CommunityInformation from '../Communities/CommunityInformation';

// API
import { useLocation } from 'react-router-dom';

// My Hooks
import { useCategoriesByCommunity } from '../../hooks/useCategoriesByCommunity'


export default function Forum() {
    // My Hooks
    const {state} = useLocation();
    const { id } = state;
    var communityID = id;

    const { categories, setCategories } = useCategoriesByCommunity(communityID);

    return (
        <>
        <CommunityInformation community={communityID}/>


        <h1>Welcome to My Forum</h1>
        <ForumPage categories={categories}/>
        
        
        </>
    )
}