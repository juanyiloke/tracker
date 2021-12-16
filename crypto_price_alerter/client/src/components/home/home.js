import React from 'react';
import './home.css';
import { Line } from 'react-chartjs-2';
import faker from 'faker';
import { Button, TextField } from '@mui/material';

import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
} from 'chart.js';

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
);

const options = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Stonk price',
      },
    },
};

const labels = [0, 1, 2, 3, 4, 5, 6, 7];

const data = {
    labels,
    datasets: [
      {
        label: 'Price',
        data: labels.map(() => faker.datatype.number({ min: 0, max: 1000 })),
        borderColor: 'rgb(255, 99, 132)',
        backgroundColor: 'rgba(255, 99, 132, 0.5)',
      }
    ],
};

class Home extends React.Component {
    constructor(props) {
        super(props)
    }

    render() {
        return (
            <div className='home-container'>
                <h1>
                    Stonks
                </h1>
                <div className='chart-container'>
                    <div className='chart'>
                        <Line
                            options={options}
                            data={data}
                        />
                    </div>
                </div>
                <div className='input-container'>
                    <div className='input-fields'>
                        <TextField
                            id='outlined-basic'
                            label='Add data'
                            variant='outlined'
                        />
                        <Button variant="contained">
                            Add
                        </Button>
                    </div>
                </div>
            </div>
        )
    }
}

export default Home