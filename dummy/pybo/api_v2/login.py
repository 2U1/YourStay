from os import access
import bcrypt
from dns import message
from flask import Flask, request, Response, jsonify, redirect, url_for, Blueprint, make_response
import json
from flask_jwt_extended.utils import get_jwt_identity
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt, generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from operator import itemgetter
from flask_cors import CORS, cross_origin
from pybo.api_v2.db import get_db

bp = Blueprint('login',__name__,url_prefix='/api/v2')

def _build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@bp.route('/login', methods=['POST', 'OPTIONS'])
@cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
def login():
    db=get_db()
    if request.is_json:
        user_id = request.json['userid']
        password = request.json['password']
    else:
        user_id = request.form['userid']
        password = request.form['password']

    
    user_info = db.user.find_one({'user_id':user_id})

    if not user_info:
        return jsonify(message="Wrong User")

    else:
        id_val = user_info['user_id']
        pwcheck = user_info['password']
        
        if bcrypt.checkpw(password.encode('utf-8'), pwcheck):
            access_token = create_access_token(identity=id_val)

            return jsonify(message="Logged In", access_token=access_token)

        else:
            return jsonify()
