import './App.css';

// My Components Imports
import MyNavBar from './components/MyNavBar';
import Landing from './pages/Landing/Landing.jsx'
import CommunityForum from './pages/Forum/CommunityForum.jsx'
import MyCommunities from './pages/Forum/MyCommunities'

// MUI Imports
import { CssBaseline } from '@mui/material';
import Container from '@mui/material/Container';

// Routing
import { Route, Routes } from "react-router-dom";

function App() {
  return (
<>
<CssBaseline>
  <Container>
      <MyNavBar/>

      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/communities" element={<MyCommunities />} />
        <Route path="/communities/forum" element={<CommunityForum />} />
      </Routes>


    </Container>
</CssBaseline>


</>
  );
}

export default App;
