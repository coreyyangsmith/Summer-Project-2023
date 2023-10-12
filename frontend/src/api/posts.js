//-------------------------------------------------------//
//  File Name: posts.js
//  Description: Utilizes axios to connect to main back-end api.
//
//  Requirements:
//      - None
//
//  Returns:
//      - REST api to selected back-end
//
// Created By: Corey Yang-Smith
// Date: October 12th, 2023
//-------------------------------------------------------//


//  IMPORTS
//-------------------------------------------------------//

// Import Axios
import axios from 'axios'


//  MAIN FUNCTION
//-------------------------------------------------------//

const axiosClient = axios.create({
    baseURL : `http://127.0.0.1:8000/api/`
});


export function getRequest(URL, payload) {
    return axiosClient.get(`/${URL}`, payload).then(response => response);
}

export function postRequest(URL, payload) {
    return axiosClient.post(`/${URL}`, payload).then(response => response);
}

export function putRequest(URL, payload) {
    return axiosClient.put(`/${URL}`, payload).then(response => response);
}

export function deleteRequest(URL, payload) {
    return axiosClient.delete(`/${URL}`, payload).then(response => response);
}