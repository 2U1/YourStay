import React, { useState } from 'react';
import Rating from 'react-simple-star-rating';
import { Link, withRouter } from 'react-router-dom';

function ScorePage() {
  const [rating1, setRating1] = useState(0) // initial rating value
  const [rating2, setRating2] = useState(0)
  const [rating3, setRating3] = useState(0)
  const [rating4, setRating4] = useState(0)
  const [total, settotal] = useState(10)
 
  // Catch Rating value
  const handleRating1 = (rate1) => {
    setRating1(rate1)
    // Some logic
  }
  const handleRating2 = (rate2) => {
    setRating2(rate2)
    // Some logic
  }
  const handleRating3 = (rate3) => {
    setRating3(rate3)
    // Some logic
  }
  const handleRating4 = (rate4) => {
    setRating4(rate4)
    // Some logic
  }

  const totalScore = (score) => {
    settotal(score)
  }



  return (
    <div className='app' style={{
        height: '100', display: 'absolute',
        flexDirection: 'column', alignItems: 'center',
        justifyContent: 'center', fontSize:'1rem'
    }}>
        <h1> Q. 당신이 중요하게 생각하는 숙소의 특징은 무엇인가요?</h1>
        <h2>(중요도에 따라 점수를 배분해 주세요!)</h2>
        <br/>
        <br/>

        <h3 style={{pading:10}} >청결도</h3>

        <Rating
            onClick={handleRating1}
            ratingValue={rating1}
            // size={20}
            stars={4}
            // label
            transition
            fillColor='orange'
            emptyColor='gray'
            className='foo1' // Will remove the inline style if applied
        />
        <br/>

        <h3 style={{padding : 10}}>편의성</h3>

        <Rating
            onClick={handleRating2}
            ratingValue={rating2}
            // size={20}
            stars={4}
            // label
            transition
            fillColor='orange'
            emptyColor='gray'
            className='foo2' // Will remove the inline style if applied
        />
        <br/>

        <h3 style={{padding:10}}>친절함</h3>

        <Rating
            onClick={handleRating3}
            ratingValue={rating3}
            // size={20}
            stars={4}
            // label
            transition
            fillColor='orange'
            emptyColor='gray'
            className='foo3' // Will remove the inline style if applied
        />
        <br/>

        <h3 style={{padding:10}}>위치</h3>

        <Rating
            onClick={handleRating4}
            ratingValue={rating4}
            // size={20}
            stars={4}
            // label
            transition
            fillColor='orange'
            emptyColor='gray'
            className='foo4' // Will remove the inline style if applied
        />
        <br />
        <br />
        <Link to='/hotel'>
          <button style={{
            color: "white",
            background: "black",
            padding: "0.375rem 0.75rem;",
            // border: "1px solid teal",
            borderRadius: ".5rem",
            fontSize: "1rem",
            lineHeight: 1.5,

          }}> next page </button>
        </Link>

    </div>
  )
}

export default withRouter(ScorePage)
