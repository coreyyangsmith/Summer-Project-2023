//-------------------------------------------------------//
//  File Name: CommunityInformation.js
//  Description: Display general information about a selected community
//
//  Requirements:
//      - Community ID
//
//  Returns:
//      - List Information regarding the Neighbourhood
//      - Provide a Leaflet Map
//
// Created By: Corey Yang-Smith
// Date: October 12th, 2023
//-------------------------------------------------------//


//  IMPORTS
//-------------------------------------------------------//

// React Import
import React, { useEffect, useState } from 'react'

// My Hooks
import { useCommunityById } from '../../hooks/useCommunityById'

// Leaflet
import { MapContainer, TileLayer, useMap } from 'react-leaflet'
import { Marker } from 'react-leaflet'
import { Popup } from 'react-leaflet'
import { Box } from '@mui/material'

//  MAIN FUNCTION
//-------------------------------------------------------//
const CommunityInformation = (props) => {
    
    const { community } = useCommunityById(props.community);
    const [position, setPosition] = useState([51.026333793586, -114.063146483044]);

    useEffect(() => {
        if (community.length > 0)
            setPosition([community[0].longitude, community[0].latitude]);    
    }, [])


                  
  return (
    <MapContainer center={position} zoom={17} scrollWheelZoom={false}>
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      <Marker position={position}>
        <Popup>
          A pretty CSS3 popup. <br /> Easily customizable.
        </Popup>
      </Marker>
    </MapContainer>)
}

//  EXPORTS
//-------------------------------------------------------//

export default CommunityInformation