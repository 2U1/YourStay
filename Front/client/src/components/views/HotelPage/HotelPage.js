import React , {useEffect, useState}from 'react';
import HotelImage from './Sections/HotelImage';
import {Row} from 'antd' ;



// 바꿀 부분
import { API_URL, API_KEY, IMAGE_BASE_URL, IMAGE_SIZE, POSTER_SIZE } from '../../Config'

import { Typography } from 'antd';

const { Title } = Typography;

function HotelPage() {
    const [Movies, setMovies] = useState([])
    const [Loading, setLoading] = useState(true)
    const [CurrentPage, setCurrentPage] = useState(0)

    useEffect(() => {
        const endpoint = `${API_URL}movie/popular?api_key=${API_KEY}&language=en-US&page=1`;
        fetchMovies(endpoint)
    }, [])



    const fetchMovies = (endpoint) => {

        fetch(endpoint)
            .then(result => result.json())
            .then(result => {
                // console.log(result)
                // console.log('Movies',...Movies)
                // console.log('result',...result.results)
                setMovies([...Movies, ...result.results])
                setCurrentPage(result.page)
            }, setLoading(false))
            .catch(error => console.error('Error:', error)
            )
    }

    const loadMoreItems = () => {
        let endpoint = '';
        setLoading(true)
        console.log('CurrentPage', CurrentPage)
        endpoint = `${API_URL}movie/popular?api_key=${API_KEY}&language=en-US&page=${CurrentPage + 1}`;
        fetchMovies(endpoint);

    }

    return (
        <div>
            <h1 style={{textAlign:'center', marginTop:'4rem', marginBottom:'4rem'}}>Hotel List</h1>

            <div style={{  width: '85%', margin: '1rem auto'}}>
            <hr />
                <Row gutter={[20, 20]}>
                    {Movies && Movies.map((movie, index) => (
                        <React.Fragment key={index}>
            
                                <HotelImage
                                    image={movie.poster_path ?
                                        `${IMAGE_BASE_URL}${POSTER_SIZE}${movie.poster_path}`
                                        : null}
                                    movieId={movie.id}
                                    movieName={movie.original_title}
                                    Text={movie.overview}
                                >
                                
                                </HotelImage>
                        </React.Fragment>
                    ))}
                </Row>
            </div>
        </div>


    )
}

export default HotelPage
