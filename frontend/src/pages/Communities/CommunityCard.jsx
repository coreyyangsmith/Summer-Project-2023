// React Import 
import React from 'react'

// MUI Import
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid'
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box'
import { createTheme, ThemeProvider } from '@mui/material';

const CommunityCard = (props) => {

    const theme = createTheme();

    theme.typography.h3 = {
    fontSize: '1.2rem',
    '@media (min-width:600px)': {
        fontSize: '1.5rem',
    },
    [theme.breakpoints.up('md')]: {
        fontSize: '2.4rem',
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
        height: 150,
        justifyContent: 'center',
        overflow: "hidden", 
        textOverflow: "ellipsis", 
    
    };

    const typographySX = {
        position: 'absolute',
        textTransform: 'uppercase',
        textAlign: 'center',
        fontSize: 22,
        color: 'black',
    }


    return(
        <Grid item xs={6}> 
            <ThemeProvider theme={theme}>
                <Paper sx={paperSX}>
                    <Box component="img"
                        padding={1}
                        sx={boxSX}
                        src={"http://127.0.0.1:8000/media/community_images/" + props.community.code + ".png"}/>
                        <Typography noWrap 
                                    variant="h3"
                                    sx={typographySX}>
                            {props.community.name}
                        </Typography>
                </Paper>     
            </ThemeProvider>            
        </Grid>                
    )
}

export default CommunityCard;