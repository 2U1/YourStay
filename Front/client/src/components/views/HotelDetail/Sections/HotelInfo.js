import React from 'react';
import { Descriptions, Badge } from 'antd';

function HotelInfo(props) {

    const { hotel } = props;
    
    return (
        <Descriptions title="Hotel Info" bordered>
        <Descriptions.Item label="Hotel Name" span={2} >{hotel.original_title}</Descriptions.Item>
        <Descriptions.Item label="Total Score" span={2} >
        {hotel.vote_average}
        </Descriptions.Item>
        <Descriptions.Item label="위치">{hotel.release_date}</Descriptions.Item>
        <Descriptions.Item label="청결도" span={2}>{hotel.revenue}</Descriptions.Item>
 

        <Descriptions.Item label="친절함">{hotel.runtime}</Descriptions.Item>
        <Descriptions.Item label="편의성" span={2}>{hotel.vote_count}</Descriptions.Item>

        </Descriptions>
    )
}

export default HotelInfo
