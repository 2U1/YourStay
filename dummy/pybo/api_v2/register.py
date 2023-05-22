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


bp = Blueprint('register',__name__,url_prefix='/api/v2')

@bp.route('/register', methods=['POST', 'OPTIONS'])
@cross_origin(origin='localhost', support_credentials=True, headers=['Content-Type','Authorization'])
def register():
    db = get_db()
    user_id = request.json['userid']
    user_name = request.json['username']
    password = request.json['password']
    clean = request.json['clean']
    conv = request.json['conv']
    kind = request.json['kind']
    position = request.json['position']

    if db.user.find_one({'user_id':user_id}):
        return jsonify(message='ID Already Exist', status='0')

    else:
        hased = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        total_sum = int(clean) + int(conv) + int(kind) + int(position)
        user_data = {'user_id':user_id, 'password':hased, 'user_name':user_name, 'cleanliness':(int(clean)/total_sum)*100, 'convenience':(int(conv)/total_sum)*100, 'kindness':(int(kind)/total_sum)*100, 'position':(int(position)/total_sum)*100}
        db.user.insert_one(user_data)

        return jsonify(message="User Registered", status='1')
