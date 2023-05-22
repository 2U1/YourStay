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

bp = Blueprint('recommended',__name__,url_prefix='/api/v2')

@bp.route('/hotels/recommended', methods=['GET'])
@jwt_required()
def recommend_hotel():
    db=get_db()
    hotels = db.hotel
    users = db.user
    current_user = get_jwt_identity()
    user_info = users.find_one({'user_id':current_user})
    user_scores = {'cleanliness':user_info['cleanliness'], 'position':user_info['position'], 'convenience': user_info['convenience'], 'kindness':user_info['kindness']}

    hotel_infos = list(hotels.find())

    weighted_scores = []

    for h in hotel_infos:
        weighted = h
        del weighted['_id']
        weighted['score'] = (user_scores['cleanliness']*h['cleanliness'] + user_scores['position']*h['position'] + user_scores['convenience']*h['convenience'] + user_scores['kindness']*h['kindness']) / 4
        weighted_scores.append(weighted)

    
    recommended = sorted(weighted_scores, key = itemgetter('totalScore'), reverse=True)[0:5]

    return jsonify({'result':recommended})
