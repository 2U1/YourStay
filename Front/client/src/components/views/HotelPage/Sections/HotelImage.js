import React from 'react';
import {Col} from 'antd' ;
import { API_URL, API_KEY, IMAGE_BASE_URL, IMAGE_SIZE, POSTER_SIZE } from '../../../Config'

function HotelImage(props) {

    let { actor, key, image, movieId, movieName, characterName, Text } = props


    if (actor) {
        return (
            <Col key={key} lg={8} md={12} xs={24}>
                <div style={{ position: 'relative' }}>
                    <img style={{ width: '100%', height: '320px' }} alt={characterName} src={`${IMAGE_BASE_URL}${POSTER_SIZE}${image}`} />
                    <div style={{ position: 'absolute', maxWidth: '500px', bottom: '2rem', marginLeft: '2rem' }} >
                        <h1 style={{ color: 'white' }} level={2} > {movieName} </h1>
                        <p style={{ color: 'white', fontSize: '1rem' }} > {Text} </p>
                    </div>
                </div>
            </Col>
        )
    } else {
        return (
            <Col key={key} lg={8} md={12} xs={24}>
                <div style={{ position: 'relative' }}>
                    <a href={`/hotel/${movieId}`} >
                        <img style={{ width: '100%', height: '320px' }} alt={movieName} src={image} />
                        <div style={{ position: 'absolute', maxWidth: '500px', bottom: '2rem', marginLeft: '2rem' }} >
                            <h1 style={{ color: 'white' }} level={2} > {movieName} </h1>
                            <p style={{ color: 'white', fontSize: '1rem' }} > {Text} </p>
                        </div>
                    </a>
                </div>
            </Col>
        )
    }

}

export default HotelImage
