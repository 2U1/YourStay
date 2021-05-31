from os import access
import bcrypt
from dns import message
from flask import Flask, request, Response, jsonify, redirect, url_for, Blueprint
import json
from flask_jwt_extended.utils import get_jwt_identity
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt, generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from operator import itemgetter
from flask_cors import CORS, cross_origin
from pybo.api_v2.db import get_db

bp = Blueprint('review',__name__,url_prefix='/api/v2')


@bp.route('/reviews/<int:hotelid>', methods=['GET'])
def get_review(hotelid):
    db=get_db()
    
    reviews = db.tokenized_review
    hotel = db.hotel
    keyword = db.keyword

    hotel_doc = hotel.find_one({'hotel_id':hotelid})
    del hotel_doc['_id']

    keyword_doc = list(keyword.find({'hotel_id':hotelid}))

    review_doc = list(reviews.find({'hotel_id':hotelid}))

    keyword_output = []

    for k in keyword_doc:
        keyword_info = {'rep':k['rep']}

        k_list = k['keywords']

        review_content = []
        review_ids = []

        pos_count = 0
        neg_count = 0

        for w in k_list:
            for r in review_doc:
                if w in r['tokens']:
                    if r['label'] == 0:
                        neg_count += 1
                    elif r['label'] == 1:
                        pos_count += 1

                    if r['reviewID'] not in review_ids:
                        keyword_reviews = {'id':r['reviewID'], 'content':r['content']}
                        review_content.append(keyword_reviews)
                        review_ids.append(r['reviewID'])
                
        keyword_info['pos'] = pos_count
        keyword_info['neg'] = neg_count
        keyword_info['reviews'] = review_content


        keyword_output.append(keyword_info)

    keyword_output_neg = sorted(keyword_output, key = itemgetter('neg'), reverse=True)[0:3]
    keyword_output_pos = sorted(keyword_output, key = itemgetter('pos'), reverse=True)[0:3]

    return jsonify({'hotel':hotel_doc, 'pos_review':keyword_output_pos, 'neg_review':keyword_output_neg})
