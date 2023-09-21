import './App.css';

// My Components Imports
import Navbar from './components/Navbar';
import Landing from './pages/Landing/Landing.jsx'
import Home from './pages/Home/Home.jsx'
import Forum from './pages/Forum/Forum.jsx'
import Communities from './pages/Communities/Communities.jsx'

import Profile from './pages/Settings/Profile';

// MUI Imports
import { CssBaseline } from '@mui/material';
import Container from '@mui/material/Container';
import { createTheme } from '@mui/material';

// Routing
import { Route, Routes } from "react-router-dom";
import { ThemeProvider } from '@emotion/react';

// Theme Definition
const myTheme = createTheme({
  palette: {
    mode: 'light',
    primary: {
      main: '#fe0000',
    },
    secondary: {
      main: '#fe7f00',
    },
  },
  typography: {
    fontFamily: [
      'inter',
      '-apple-system',
      'BlinkMacSystemFont',
      '"Segoe UI"',
      'Roboto',
      '"Helvetica Neue"',
      'Arial',
      'sans-serif',
      '"Apple Color Emoji"',
      '"Segoe UI Emoji"',
      '"Segoe UI Symbol"',
    ].join(','),
  },  
});

const App = () => {
  return (
<>
<ThemeProvider theme={myTheme}>
  <CssBaseline>

        <Navbar/>

        <Container>
          <Routes>
            <Route path="/" element={<Landing />} />
            <Route path="/home" element={<Home />} />            
            <Route path="/communities" element={<Communities />} />
            <Route path="/communities/:code" element={<Forum code={823}/>}/>     
            <Route path="/forum" element={<Forum />} />

            <Route path="/profile" element={<Profile />} />            
          </Routes>
        </Container>

  </CssBaseline>
</ThemeProvider>
</>
)};

export default App;
