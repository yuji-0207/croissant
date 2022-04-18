import React from 'react';

import axios from 'axios';

import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Stack from '@mui/material/Stack';
import { styled } from '@mui/material/styles';


function get(setLayers) {

    axios.get('http://127.0.0.1:8000/layers/')
  
        .then(res => {
            setLayers(res.data);
        })
        
        .catch(err => {
           console.log(err);
        });

};


const Item = styled(Paper)(({ theme }) => ({
    backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
    ...theme.typography.body2,
    padding: theme.spacing(1),
    textAlign: 'center',
    color: theme.palette.text.secondary,
}));


export default function LayersGet({lastCreated}) {

    const [layers, setLayers] = React.useState([]);
    React.useEffect(() => {get(setLayers)}, [lastCreated]);

    return (
        <Box sx={{ width: '50%' }}>
            <Stack spacing={2}>
                {
                    layers.map(layer => (
                        <Item>
                            <p>{layer.title}</p>
                            <p>{layer.description}</p>
                            <p>{layer.parent}</p>
                            <p>{layer.startDate}</p>
                            <p>{layer.startTime}</p>
                            <p>{layer.endDate}</p>
                            <p>{layer.endTime}</p>
                        </Item>
                    ))
                }
            </Stack>
        </Box>
    )
}
