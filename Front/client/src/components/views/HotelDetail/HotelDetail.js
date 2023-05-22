import React ,{useState, useEffect} from 'react';
import { API_URL, API_KEY , IMAGE_BASE_URL, IMAGE_SIZE} from '../../Config';
import MainImage from '../HotelPage/Sections/MainImage'
import HotelInfo from './Sections/HotelInfo'



function HotelDetail(props) {

    let movieId = props.match.params.movieId

    const [Hotel, setHotel] = useState([])



    useEffect(() => {
        let endpointCrew = `${API_URL}movie/${movieId}/credits?api_key=${API_KEY}&language=en-US`
        let endpointInfo = `${API_URL}movie/${movieId}?api_key=${API_KEY}&language=en-US`
        fetch(endpointInfo)
        .then(response => response.json())
        .then(response =>{
            console.log(response)
            setHotel(response)
        })
        
    }, [])





    const [ActorToggle, setActorToggle] = useState(false)

    const toggleActorView = () => {
        setActorToggle(!ActorToggle)
    }

    return (
        <div style={{width:'100%', margin:'0'}}>
            {/* Header */}
            {/* {!LoadingForMovie ? */}
                <MainImage
                    image={`${IMAGE_BASE_URL}${IMAGE_SIZE}${Hotel.backdrop_path}`}
                    title={Hotel.original_title}
                    text={Hotel.overview}
                />
                {/* <div>loading...</div> */}
            {/* }


            {/* Body */}
            <div style={{ width: '85%', margin: '1rem auto' }}>

                {/* <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
                    <Favorite movieInfo={Movie} movieId={movieId} userFrom={localStorage.getItem('userId')} />
                </div> */}
                {/* // Movie Info */}
                {/* {!LoadingForMovie ? */}
                    <HotelInfo style={{}} hotel={Hotel} /> 
                    {/* <div>loading...</div> */}
                {/* } */}
</div>
             <br />
            {/* Actors Grid*/}

                {/* <div style={{ display: 'flex', justifyContent: 'center', margin: '2rem' }}>
                    <Button onClick={toggleActorView}>Toggle Actor View </Button>
                </div> */}
{/* 
                {ActorToggle &&
                    <Row gutter={[16, 16]}>
                        {
                            !LoadingForCasts ? Casts.map((cast, index) => (
                                cast.profile_path &&
                                <GridCards actor image={cast.profile_path} characterName={cast.characterName} />
                            )) :
                                // <div>loading...</div>
                        } */}
                    {/* </Row>
                } */}
                <br />

                {/* <div style={{ display: 'flex', justifyContent: 'center' }}>
                    <LikeDislikes video videoId={movieId} userId={localStorage.getItem('userId')} />
                </div> */}

                {/* Comments */}
                {/* <Comments movieTitle={Movie.original_title} CommentLists={CommentLists} postId={movieId} refreshFunction={updateComment} />

            </div> */}
        </div>
    )
}

export default HotelDetail
