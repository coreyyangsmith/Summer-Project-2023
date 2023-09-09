//MUI Imports
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid'
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box'


const CommunityCard = (community) => {
    const paperSX = {
        boxShadow: 3,
        "&:hover": {
          boxShadow: 8,
        },
      };
    return(
        <Grid item xs={3}>
            <Paper sx={paperSX}>
                <Box paddingX={1}
                sx={{
                    width:200,
                    height:150,
                    overflow: 'auto'
                }}>

                    <Typography component="h2" variant='subtitle1'>
                        {community.name}
                    </Typography>

                    <Typography component="h3" variant="subtitle2">
                        Sector: {community.sector}
                    </Typography>

                    <img src={community.image}></img>

                    
                </Box>
            </Paper>
            </Grid>            
    )
}

export default CommunityCard;

/*
Perhaps need to fetch the primary and secondary muscles API, and query/map the array
of IDs to their corresponding names to properly display the muscles.
*/