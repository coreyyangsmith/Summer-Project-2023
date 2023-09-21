// React Import
import React from 'react'

// Routing
import { useNavigate } from 'react-router-dom';

// MUI Import
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid'
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box'
import { createTheme, ThemeProvider } from '@mui/material';


const ForumCard = (props) => {

  const theme = createTheme();
  const navigate = useNavigate();

  const handleClick = () => {
      console.log(props.category.name);
      }

  theme.typography.h3 = {
  fontSize: '0.9rem',
  '@media (min-width:600px)': {
      fontSize: '1.3rem',
  },
  [theme.breakpoints.up('md')]: {
      fontSize: '2.1rem',
  },
  };

  const paperSX = {
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',        
      boxShadow: 3,       
      "&:hover": {
        boxShadow: 12,
      },
  };

  const boxSX = {
      display: 'flex',
      width: 400,
      height: 100,
      justifyContent: 'center',
      overflow: "hidden", 
      textOverflow: "ellipsis", 
      objectFit: 'cover'
  };

  const typographySX = {
      position: 'absolute',
      textTransform: 'uppercase',
      textAlign: 'center',
      fontSize: 22,
      color: 'black',
  }


  return (
    <Grid item xs={12}> 
    <ThemeProvider theme={theme}>
        <Paper sx={paperSX}>
            <Box padding={0.5}
                sx={boxSX}
                onClick={handleClick}/>
                <Typography noWrap 
                            variant="h3"
                            sx={typographySX}>
                    {props.category.name}
                </Typography>                       
        </Paper>     
    </ThemeProvider>            
</Grid>    
  )
}

export default ForumCard